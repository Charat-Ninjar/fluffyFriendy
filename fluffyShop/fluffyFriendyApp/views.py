from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from fluffyFriendyApp.models import Product, Cart
from .forms import ProductForm
from .models import Product, Cart, CartProduct
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart_index.html")

def form(request):
    return HttpResponse("<h1> Form </h1>")

def login_form(request):
    return render(request, "login_form.html")

def signup_form(request):
    return render(request, "signup_form.html")

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user 
    cart, created = Cart.objects.get_or_create(user=user)
    CartProduct.objects.create(cart=cart, product=product)
    return redirect('/')

@login_required
def view_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user, checkout_status=False).first()
    print("test view_cart")
    if cart:
        cart_products = CartProduct.objects.filter(cart=cart)
        product_summary = {}
        subtotal = 0
        for cart_product in cart_products:
            product = cart_product.product
            if product.name in product_summary:
                product_summary[product.name]['quantity'] += cart_product.quantity
            else:
                product_summary[product.name] = {
                    'price': product.price,
                    'quantity': cart_product.quantity,
                    'image': product.image
                }
            product_summary[product.name]['total_price'] = product_summary[product.name]['price'] * product_summary[product.name]['quantity']
            subtotal += product_summary[product.name]['total_price']
        total_price = subtotal
        return render(request, "cart.html", {"product_summary": product_summary, "subtotal": subtotal, "total_price": total_price})
    else:
        return render(request, "cart_index.html")


def signup(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.create_user(username=username,password=password)
    user.save()
    print("test user", user)
    return render(request,"login_form.html")

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None :
        auth.login(request, user)
        return redirect('/')
    else :
        messages.info(request,"user or password invalid")
        return redirect('/login_form')

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
            return redirect('/') 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def remove_item(request, product_id):
    try:
        CartProduct.objects.filter(cart=request.user.cart, product_id=product_id).delete()
        return redirect('/cart_index')
    except Exception as e:
        # Log the error or return an error response
        print("Error removing item:", e)
        return HttpResponseServerError("Error removing item")

def increase_item(request, product_id):
    try:
        product = get_object_or_404(CartProduct, pk=product_id)
        product.quantity += 1
        product.save()
        return redirect('/cart_index')
    except Exception as e:
        # Log the error or return an error response
        print("Error increasing item quantity:", e)
        return HttpResponseServerError("Error increasing item quantity")