from django.urls import path
from fluffyFriendyApp import views

urlpatterns = [
    path('', views.index ),
    path('cart', views.cart),
    path('form', views.form)
]
