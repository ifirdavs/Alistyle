"""Alistyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('wishlist', WishlistProductsView.as_view(), name="wishlist"),
    path('wishlist/delete/<int:pk>', wishlist_pr_delete),
    path('wishlist/add/<int:pk>', AddToWishlistView.as_view(), name='addtowishlist'),

    path('shopcart', CartView.as_view(), name="shopcart"),
    path('shopcart/cart_plus/<int:pk>', cart_plus),
    path('shopcart/cart_minus/<int:pk>', cart_minus),
    path('shopcart/add/<int:pk>', AddToCartView.as_view(), name="addtocart"),
    path('shopcart/delete/<int:pk>', cart_pr_delete),
    
    path('orders', OrderView.as_view(), name="orders"),

    path('addneworder', AddNewOrderView.as_view(), name="addneworder"),
]
