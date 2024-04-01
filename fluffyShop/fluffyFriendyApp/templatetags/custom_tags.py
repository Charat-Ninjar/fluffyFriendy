from django import template
from django.template.loader import render_to_string
from fluffyFriendyApp.models import Product, User, Cart, CartProduct
from collections import defaultdict

register = template.Library()

@register.simple_tag(takes_context=True)
def productCard(context):
    # Implement your logic here to fetch product data and render the HTML for the card
    # For demonstration purposes, let's assume you have a list of products
    products = Product.objects.all()
    return render_to_string('product_card_template.html', {'card_collection': products})

@register.simple_tag(takes_context=True)
def view_cart_custom(context):
    print("View Cart Custom tag called.")
    mock_user_id = 2
    try:
        user = User.objects.get(pk=mock_user_id)
        print("user:", user)
        cart = Cart.objects.filter(user=user, checkout_status=False).first()
        cart_products = CartProduct.objects.filter(cart=cart) if cart else []

        product_summary = {}
        for cart_product in cart_products:
            product = cart_product.product
            if product.name in product_summary:
                product_summary[product.name]['quantity'] += cart_product.quantity
            else:
                product_summary[product.name] = {
                    'price': product.price,
                    'quantity': cart_product.quantity
                }


        print("Cart Items:", product_summary)

        for product_name, data in product_summary.items():
            data['total_price'] = data['price'] * data['quantity']

        return render_to_string("cart.html", {"product_summary": product_summary})
    except User.DoesNotExist:
        print("User with ID 1 does not exist.")
        return ''