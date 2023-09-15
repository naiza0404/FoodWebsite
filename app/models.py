from django.db import models

# Create your models here.



class Category(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='',unique=True)

    def __str__(self):
      
      return self.name
    

class Customer(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')
    

class Product(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    
    
    def __str__(self):
        return self.name
    


class Admin(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='products/',default='') 
    title = models.CharField(max_length=100,default='')
    price = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=100,default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)



class Cart(models.Model):
    id =  models.AutoField(primary_key=True)
    users = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='cart/',default='')
    title = models.CharField(max_length=100,default='')
    price = models.CharField(max_length=100,default='')
    quantity = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.title
    

    def caculate(self):
        return float(self.price) * int( self.quantity)
    

class checkout(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')
    price = models.CharField(max_length=255,default='')


    
    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')
    date = models.DateField(auto_now=True)
    time_field = models.TimeField(auto_now=True)
    person = models.CharField(max_length=100,default='')


    def  __str__(self):
        return self.name
    