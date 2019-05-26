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
        self.customer_id = customer_id

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
        return cart['items']

    def edit_item_from_cart(self, customer_id, request_data):
        pass