from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from fluffyFriendyApp.models import User, Product, Cart
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductForm
import logging

# Create your views here.

def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart_index.html")

def form(request):
    return HttpResponse("<h1> Form </h1>")



def remove_product_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if 'cart' in request.session:
        cart = request.session['cart']
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart

    return redirect('/') 

def remove_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    product.delete()
    
    return redirect('/')

def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def search_product(request):
    query = request.GET.get('query')
    if query:
        search_results = Product.objects.filter(name__icontains=query)
    else:
        search_results = None
        return redirect('/')
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    try:
        user = User.objects.get(name='mock_user')
    except User.DoesNotExist:
        user = User.objects.create(name='mock_user')
    
    cart, created = Cart.objects.get_or_create(user=user)
    
    cart.products.add(product)
    
    return redirect('/')

def view_cart(request):
    user = 'mock_user' 

    cart = Cart.objects.filter(user=user, checkout_status=False).first() 
    if cart:
        cart_items = "test"
    else:
        cart_items = ["test"] 


    cart_items = "test..."
    return render(request, "cart.html", {"items": cart_items})