from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def form(request):
    return HttpResponse("<h1> Form </h1>")