from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name="index_page"),
    path('signup/',signup,name="siginup-page"),
    path('login/',login,name="login-page"),
    path('admin_login/',adminlogin,name="admin-login"),
    path('success/',success,name="success-page"),
    path('logout/',logout,name="logout"),
    path('admin_layout/',admin,name="admin_page"),
    path('admin_layout/edit/<int:pk>/',edit,name="edit-function"),
    path('admin_layout/insert_admin/',insert,name="insert-page"),
    path('admin_layout/products/',products,name="products-page"),
    path('admin_layout/users/',users,name="users-page"),
    path('admin_layout/delete/<int:pk>/',delete,name="delete-function"),
    path('about/',about,name="about-page"),
    path('cart/<int:pk>/',cart,name="cart-page"),
    path('deleteitem/<int:pk>/',delete_cart_item,name="delete-cart"),
    path('checkout/',checkout,name="chechout-page"),
    path('blog/',blog,name="blog-page"),
    path('contact/',contact,name="contact-page"),
    path('reservation/',reservation,name="reservation"),
    path('admin_layout/reservation/',reservationdata,name="reservation-table")
    
]
