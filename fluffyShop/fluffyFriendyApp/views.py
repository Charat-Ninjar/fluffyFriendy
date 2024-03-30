from django.shortcuts import render
from django.http import HttpResponse
from fluffyFriendyApp.models import User, Product, Cart
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
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
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

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
            return redirect('/')  # Redirect to the desired page after editing
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def search_product(request):
    query = request.GET.get('query')
    if query:
        # Perform a search query using your Product model
        search_results = Product.objects.filter(name__icontains=query)
    else:
        search_results = None
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})
