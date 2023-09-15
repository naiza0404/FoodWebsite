from django.contrib import admin
from .models import Product,Category,Customer,Admin,Cart,checkout,Reservation

# Register your models here.

class ProductTable(admin.ModelAdmin):
    list_display = ('id','image','title','price','description','category')

admin.site.register(Product,ProductTable)


class CategoryTable(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Category,CategoryTable)

class CustomerTable(admin.ModelAdmin):
    list_display = ('id','name','email','password')

admin.site.register(Customer,CustomerTable)

class AdminTable(admin.ModelAdmin):
    list_display = ('id','name','email','password')

admin.site.register(Admin,AdminTable)

class CartTable(admin.ModelAdmin):
    list_display = ('id','users','image','title','price','quantity','description')

admin.site.register(Cart,CartTable)

admin.site.register(checkout)


class ReservationTable(admin.ModelAdmin):
    list_display = ('id','name','email','phone','date','time_field','person')


admin.site.register(Reservation,ReservationTable)