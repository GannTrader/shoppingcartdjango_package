from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponse
# Create your views here.
def index(request):
	products = Product.objects.all()
	return render(request, 'home/index.html', {'products': products})

# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'home/cart/cart_detail.html')
    # return HttpResponse('hello')