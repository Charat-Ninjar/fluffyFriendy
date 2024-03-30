from django.shortcuts import render
from django.http import HttpResponse
from fluffyFriendyApp.models import User, Product, Cart
from django.shortcuts import render, redirect
from .forms import ProductForm


# Create your views here.

def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def form(request):
    return HttpResponse("<h1> Form </h1>")


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('product_list')  # Redirect to product list page or any other page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
