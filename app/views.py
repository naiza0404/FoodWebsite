from collections import Counter
import hashlib
from cv2 import sumElems
from django.shortcuts import get_object_or_404, render,redirect
from .models import Customer,Admin,Product,Category,Cart
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Sum


# Create your views here.

def index(request):
    

    user_email = request.session.get('user_email')
    if user_email:

        categories = Category.objects.all()

        products_by_category = {}

        for category in categories:
            products_by_category[category.name] = Product.objects.filter(category=category)

        context = {
            'products_by_category': products_by_category
        }

        return render(request,'index.html',context)
    
    else:
        alert_message = "Please sign up to access this content."
      
        

        context = {
            'error_message':alert_message,
        }

        return render(request, 'index.html', context)
    
def signup(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        your_email = request.POST.get('your_email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Perform form validation
        if not username or not your_email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check if user already exists
        if Customer.objects.filter(email=your_email).exists():
            messages.error(request, "email already exists.")
            context = {
                'error_message':"Email already exists"
            }
            return render(request, 'signup.html',context)

        # Your registration logic here (e.g., creating a user account)
        # Save the user with a hashed password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        user = Customer(name=username, email=your_email, password=hashed_password)
        user.save()

        # Optionally, you can log the user in after registration
        # You might need to import necessary modules and use the appropriate methods
        # ...

        # Redirect to a success page or another view
        return redirect('/success')  # Change 'success_page' to the appropriate URL name

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        your_email = request.POST.get('your_email')
        password = request.POST.get('password')

        if not your_email or not password:
            return render(request, 'login.html', {'error_message': "All fields are required."})

        try:
            user = Customer.objects.get(email=your_email)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == user.password:
                # Successfully logged in
                request.session['user_email'] = your_email
                return redirect('/')  # Change to the appropriate URL
            else:
                return render(request, 'login.html', {'error_message': "Invalid credentials."})
        except Customer.DoesNotExist:
            return render(request, 'login.html', {'error_message': "User does not exist. Please register."})

    return render(request, 'login.html')

def success(request):
    return render(request,'success_page.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def adminlogin(request):

    if request.method == 'POST':
        your_email = request.POST.get('your_email')
        password = request.POST.get('password')
        
        try:
            admin = Admin.objects.get(email=your_email)
        except:
            error_message = "Admin not found. Please check your credentials or contact with owner"
            return render(request, 'admin_template/login.html', {'error_message': error_message})
        
        # Here you can add further logic to check the password and handle the login process
        
        # Redirect to the front page
        return redirect('/admin_layout/')  # Change 'front_page' to the URL name of your front page view
    
    return render(request,'admin_template/login.html')

def admin(request):

    Product_data = Product.objects.all()
    total = Product_data.count()
    category = Category.objects.count()
    total_price = sum(int(product.price) for product in Product_data)
    customer = Customer.objects.count()


    
    context = {
        'Products':Product_data,
        'total_product':total,
        'total_category':category,
        'total_price':total_price,
        'total_customer':customer
    }
    return render(request,'admin_template/admin.html',context)

def insert(request):

    if request.method == 'POST':
        # try:
            title = request.POST.get('title')
            price = request.POST.get('price')
            description = request.POST.get('description')
            category_id = request.POST.get('category')

            image = request.FILES.get('image')

            category_instance = Category.objects.get(pk=category_id)
            product = Product(
                title=title,
                description=description,
                price=price,
                image=image,    
                category=category_instance,
            )

            product.save()

            context = {
                'error_message':"Product Inserted Successfully"
            }

            return render(request,'admin_template/insert.html',context)

    category_data = Category.objects.all()
    context = {
        'category':category_data
    }

    return render(request,'admin_template/insert.html',context)

def edit(request, pk):
    # Get the product instance to be edited
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        # try:
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category_id = request.POST.get('category')

        image = request.FILES.get('image')

        category_instance = Category.objects.get(pk=category_id)

        # Update the fields of the existing product
        product.title = title
        product.description = description
        product.price = price
        product.image = image
        product.category = category_instance

        product.save()

        context = {
            'error_message': "Product Updated Successfully"
        }

        return render(request, 'admin_template/edit.html', context)

    category_data = Category.objects.all()
    context = {
        'category': category_data,  
        'product': product 
    }

    return render(request, 'admin_template/edit.html', context)

def products(request):
    Product_data = Product.objects.all()
    
    context = {
        'Products':Product_data,
    }
    return render(request,'admin_template/products.html',context)

def users(request):

    customer_data = Customer.objects.all()
    
    context = {
        'customer':customer_data,
    }

    return render(request,'admin_template/users.html',context)

def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product:
        product.delete()
        Product_data = Product.objects.all()
        total = Product_data.count()
        category = Category.objects.count()
        total_price = sum(int(product.price) for product in Product_data)
        customer = Customer.objects.count()


    
        context = {
            'Products':Product_data,
            'total_product':total,
            'total_category':category,
            'total_price':total_price,
            'total_customer':customer,
            'error_message':"Product Deleted Successfully"
        }
        return render(request,'admin_template/admin.html',context)
    
def about(request):
    return render(request,'about.html')

def cart(request,pk):

    try:
        product = Product.objects.get(pk=pk)

        user_email = request.session.get('user_email')

        product_users = user_email
        product_image = product.image
        product_title = product.title
        product_price = product.price
        product_description = product.description

        cart_item = Cart(users=product_users,image=product_image,title=product_title,price=product_price,quantity='1',description=product_description)
        cart_item.save()

        cart_data = Cart.objects.all()
        total_products = cart_data.count()


        total_price = cart_data.aggregate(total_price=Sum('price'))['total_price']


        context = {
            'cart':cart_data,
            'total':total_price,
            'total_products':total_products
            
        }


        return render(request,'cart.html',context)

        
    except:
        pass

    return render(request,'cart.html')


def delete_cart_item(request,pk):

    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()

    cart_data = Cart.objects.all()
    total_products = cart_data.count()
    total_price = cart_data.aggregate(total_price=Sum('price'))['total_price']


    context = {
        'cart':cart_data,
        'total':total_price,
        'total_products':total_products
    }


    return render(request,'cart.html',context)  

def checkout(request):

    email = request.session.get('user_email')
    cart_items = Cart.objects.filter(users=email)    
    cart_items.delete()

    context = {
        'error_message':"payment successfully"
    }



    return render(request,'check_out.html',context)


def blog(request):
    return render(request,'blog.html')