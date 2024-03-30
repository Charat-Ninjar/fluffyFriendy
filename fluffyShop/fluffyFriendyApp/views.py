from django.shortcuts import render
from django.http import HttpResponse
from fluffyFriendyApp.models import User, Product, Cart
# Create your views here.

def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def form(request):
    return HttpResponse("<h1> Form </h1>")

def product_card(request):
    owner_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "car_detail.html", context)

