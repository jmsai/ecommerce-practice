from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from model.Cart import Cart
import view.Cart as view

model = Cart()

def show_all_inside_cart(customer_id):
    cart = model.find_cart_by_customer_id(customer_id)
    return view.cart_response(cart)