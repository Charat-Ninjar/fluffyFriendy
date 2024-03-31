from django import template
from django.template.loader import render_to_string
from fluffyFriendyApp.models import Product, User, Cart
register = template.Library()

@register.simple_tag(takes_context=True)
def productCard(context):
    # Implement your logic here to fetch product data and render the HTML for the card
    # For demonstration purposes, let's assume you have a list of products
    products = Product.objects.all()
    return render_to_string('product_card_template.html', {'card_collection': products})

@register.simple_tag(takes_context=True)
def view_cart(takes_context=True):
    user = 'mock_user' 

    # user name 'mock_user' user_id in database is 2
    # has cart_id 2 have 2 product_id 2 and 8
    # in cart_items should have product_id 2 and 8 and display

    cart = Cart.objects.filter(user=user, checkout_status=False).first() 
    if cart:
        cart_items = cart.products.all()  
    else:
        cart_items = [] 

    return render_to_string("cart.html", {"items": cart_items})

#  products = [
#         {'name': 'Product 1', 'description': 'Description of Product 1', 'price': 10,'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 2', 'description': 'Description of Product 2', 'price': 20, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 3', 'description': 'Description of Product 3', 'price': 30, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 4', 'description': 'Description of Product 1', 'price': 10,'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 5', 'description': 'Description of Product 2', 'price': 20, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 6', 'description': 'Description of Product 3', 'price': 30, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#     ]