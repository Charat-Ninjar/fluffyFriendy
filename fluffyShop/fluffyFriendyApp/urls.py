from django.urls import path
from fluffyFriendyApp import views
from .views import add_product, edit_product, search_product, add_to_cart

urlpatterns = [
    path('', views.index),
    path('cart_index/', views.cart),
    path('form/', views.form),
    path('add/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('search/', search_product, name='search_product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
]
