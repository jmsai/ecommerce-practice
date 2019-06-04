from helpers.v2.FilterHelper import filter_result
from helpers.v2.FilterHelper import remove_data
from helpers.v2.GenerateHelper import generate_id

import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
carts = []


class CartModel:
    def __init__(self, customer_id='', items='', payment_total=''):
        self._id = generate_id
        self.customer_id = customer_id
        self.items = items
        self.payment_total = payment_total

    def add(self, new_cart):
        carts.append(new_cart)

    def find_all(self):
        return carts

    def find_by_customer(self, customer_id):
        carts = self.find_all()
        cart = filter_result('customer_id', customer_id, carts)
        return next(cart, None)

    def find_all_items(self, customer_id):
        cart = self.find_by_customer(customer_id)
        return cart['items']

    def add_item(self, items, data):
        for item in items:
            if item['item_id'] == data['item_id']:
                item['quantity'] += data['quantity']
        items.append(data)
        return items

    def edit_item(self, items, item_id, data):
        item = next(filter_result('item_id', item_id, items), None)
        if item is not None:
            item['quantity'] += data['quantity']
        return items

    def remove_item(self, items, item_id):
        item = next(remove_data('item_id', item_id, items), None)
        if item is not None:
            items.remove(item)
        return items
