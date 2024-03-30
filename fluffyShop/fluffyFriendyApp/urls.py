from django.urls import path
from fluffyFriendyApp import views
from .views import add_product, edit_product, search_product

urlpatterns = [
    path('', views.index),
    path('cart/', views.cart),
    path('form/', views.form),
    path('add/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('search/', search_product, name='search_product'),
]
