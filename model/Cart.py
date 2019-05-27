import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from helper.Helper import generate_id

class Cart:
    def __init__(self, customer_id='', items='', payment_total=''):
        self.customer_id = customer_id
        self.items = items
        self.payment_total = payment_total

    def find_all_carts(self):
        with open('seed.json', 'r') as seed_file:
            data = json.load(seed_file)
            return data["carts"]

    def find_cart_by_customer_id(self, customer_id):
        carts = self.find_all_carts()
        cart = next(filter(lambda data: data['customer_id'] == customer_id, carts), None)
        return cart

    def add_item_to_cart(self, customer_id, request_data):
        cart = self.find_cart_by_customer_id(customer_id)
        items = cart['items']
        for item in items:
            if item['item_id'] == request_data['item_id']:
                item['quantity'] += request_data['quantity']
                return cart
        items.append(request_data)
        return cart

    def edit_item_from_cart(self, customer_id, request_data):
        cart = self.find_cart_by_customer_id(customer_id)
        items = cart['items']
        item = next(filter(lambda data: data['item_id'] == request_data['item_id'], items), None)
        if item is None:
            items.append(request_data)
        else:
            item.update(request_data)
        return items