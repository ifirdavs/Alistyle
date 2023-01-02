from django.shortcuts import render, redirect

from django.views import View

from.models import *
from userapp.models import Profile
from mainapp.models import Product

from django.db.models import Sum

# Create your views here.

class WishlistProductsView(View):
    def get(self, request):
        data = {
            'list': Wishlist.objects.filter(profile__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', data)

class AddToWishlistView(View):
    def get(self, request, pk):
        p = Profile.objects.get(user=request.user)
        c = CartItem.objects.get(id=pk)
        if len(Wishlist.objects.filter(product=c.product)) == 0:
            Wishlist.objects.create(
                profile=p,
                product=c.product,
            )
        
        return redirect('/shopcart')

def wishlist_pr_delete(request, pk):
    Wishlist.objects.get(id=pk).delete()
    return redirect('/wishlist')

class CartView(View):
    def get(self, request):
        cart = CartItem.objects.filter(profile__user=request.user)
        total = 0
        for i in cart:
            total += i.total
        discount = 0
        for i in cart:
            discount += int(i.product.discount * i.product.price / 100 * i.quantity)
        data = {
            'cart': cart,
            'total': total,
            'discount': discount,
            't': total - discount
        }
        return render(request, 'page-shopping-cart.html', data)

class OrdersView(View):
    def get(self, request):
        data = {
            
        }
        return render(request, 'page-profile-orders.html', data)

def cart_plus(request, pk):        ## request is a must
    cart = CartItem.objects.get(id=pk)
    if cart.quantity != 10:
        cart.quantity += 1
    cart.total = cart.quantity * cart.product.price
    cart.save()
    return redirect("/shopcart")

def cart_minus(request, pk):        ## request is a must
    cart = CartItem.objects.get(id=pk)
    if cart.quantity != 1:
        cart.quantity -= 1
    cart.total = cart.quantity * cart.product.price
    cart.save()
    return redirect("/shopcart")

class AddToCartView(View):
    def get(self, request, pk):
        prof = Profile.objects.get(user=request.user)
        prod = Product.objects.get(id=pk)
        crt = CartItem.objects.filter(product=prod, profile=prof)
        if len(crt) > 0:
            return redirect('/shopcart')
        CartItem.objects.create(
            product = prod,
            profile = prof,
            total = prod.price
        )
        return redirect('/shopcart')

def cart_pr_delete(request, pk):                            ## request is a must
    CartItem.objects.get(id=pk).delete()
    return redirect('/shopcart')

class OrderView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'orders': Order.objects.filter(profile__user=request.user)
            }
            return render(request, 'page-profile-orders.html', data)
        return redirect('login')

class AddNewOrderView(View):
    def get(self, request):
        carts = CartItem.objects.filter(profile__user=request.user)
        order = Order.objects.create(
            profile=Profile.objects.get(user=request.user),
            items_total=carts.aggregate(Sum('total')).get('total__sum'),
            total=int(carts.aggregate(Sum('total')).get('total__sum')) + 5,
        )
        for i in carts:
            order.cart.add(i.id)
        order.save()
        return redirect('/orders')