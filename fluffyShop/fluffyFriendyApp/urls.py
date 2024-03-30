from django.urls import path
from fluffyFriendyApp import views
from .views import add_product

urlpatterns = [
    path('', views.index ),
    path('cart', views.cart),
    path('form', views.form),
    path('add', add_product, name='add_product')
]
