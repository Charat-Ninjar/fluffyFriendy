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


#  products = [
#         {'name': 'Product 1', 'description': 'Description of Product 1', 'price': 10,'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 2', 'description': 'Description of Product 2', 'price': 20, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 3', 'description': 'Description of Product 3', 'price': 30, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 4', 'description': 'Description of Product 1', 'price': 10,'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 5', 'description': 'Description of Product 2', 'price': 20, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#         {'name': 'Product 6', 'description': 'Description of Product 3', 'price': 30, 'image_url': 'https://www.mariskavos.nl/wp-content/uploads/2023/06/free-alpaca-crochet-pattern-2.webp'},
#     ]