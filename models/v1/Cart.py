from helpers.Helper import filter_result
from helpers.Helper import remove_data

import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
carts = []


class Cart:
    __payment_total = 0

    def __init__(self, customer_id='', items=''):
        self.customer_id = customer_id
        self.items = items

    def add(self, new_cart):
        carts.append(new_cart)

    def find_all(self):
        return carts

    def find_by_customer(self, customer_id):
        carts = self.find_all()
        customer = filter_result('customer_id', customer_id, carts)
        return next(customer, None)

    def add_item(self, customer_id, request_data):
        cart = self.find_by_customer(customer_id)
        items = cart['items']
        for item in items:
            if item['item_id'] == request_data['item_id']:
                item['quantity'] += request_data['quantity']
                return cart
        items.append(request_data)
        return cart

    def edit_item(self, customer_id, item_id, data):
        cart = self.find_by_customer(customer_id)
        items = cart['items']
        item = next(filter_result('item_id', item_id, items), None)
        if item is None:
            return item
        item['quantity'] += data['quantity']
        return cart

    def remove_item(self, customer_id, item_id):
        cart = self.find_by_customer(customer_id)
        items = cart['items']
        item = next(filter_result('item_id', item_id, items), None)
        if item is None:
            return item
        items.remove(item)
        return cart
