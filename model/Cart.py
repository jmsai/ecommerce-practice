import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import generate_id

class Cart:
    def __init__(self, items, payment_total, customer_id):
        self.cart_id = generate_id()
        self.items = items
        self.payment_total = payment_total
        self.customer_id = customer_id

    def find_all_carts(self):
        with open('seed.json', 'r') as seed_file:
            data = json.load(seed_file)
            return data["carts"]

    def find_cart_by_customer_id(self, customer_id):
        carts = self.find_all_carts()
        for cart in carts:
            if cart["customer_id"] == customer_id:
                return cart
        return { "message": "User does not exist" }