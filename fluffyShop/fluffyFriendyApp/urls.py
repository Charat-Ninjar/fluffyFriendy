from django.urls import path
from fluffyFriendyApp import views
from .views import add_product, edit_product, search_product, add_to_cart

urlpatterns = [
    path('', views.index),
    path('login_form/', views.login_form),
    path('cart_index/', views.cart),
    path('form/', views.form),
    path('add/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('search/', search_product, name='search_product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('signup_form/', views.signup_form),
    path('signup/', views.signup, name='signup'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_item/<int:product_id>/', views.remove_item, name='remove_item'),
    path('increase_item/<int:product_id>/', views.increase_item, name='increase_item'),
    path('login/', views.login, name='login')

]
