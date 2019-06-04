from helper.Helper import filter_result, remove_data

import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
carts = []


class Cart:
    def __init__(self, customer_id='', items='', payment_total=''):
        self.customer_id = customer_id
        self.items = items
        self.payment_total = payment_total

    def create_cart_for_user(self, new_cart):
        carts.append(new_cart)

    def find_all_carts(self):
        return carts

    def find_cart_by_customer_id(self, customer_id):
        carts = self.find_all_carts()
        cart = filter_result('customer_id', customer_id, carts)
        return next(cart, None)

    def add_item_to_cart(self, customer_id, request_data):
        cart = self.find_cart_by_customer_id(customer_id)
        items = cart['items']
        for item in items:
            if item['item_id'] == request_data['item_id']:
                item['quantity'] += request_data['quantity']
                return cart
        items.append(request_data)
        return cart

    def edit_item_from_cart(self, customer_id, item_id, data):
        cart = self.find_cart_by_customer_id(customer_id)
        items = cart['items']
        item = next(filter_result('item_id', item_id, items), None)
        if item is not None:
            item['quantity'] += data['quantity']
        return cart

    def remove_item_from_cart(self, customer_id, item_id):
        cart = self.find_cart_by_customer_id(customer_id)
        items = cart['items']
        item = next(remove_data('item_id', item_id, items), None)
        if item is not None:
            items.remove(item)
        return cart
