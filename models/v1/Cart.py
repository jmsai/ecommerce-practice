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

    def add_item(self, customer_id, data):
        cart = self.find_by_customer(customer_id)
        items = cart['items']
        for item in items:
            if item['item_id'] == data['item_id']:
                item['quantity'] += data['quantity']
                return cart
        items.append(data)
        return cart

    def edit_item(self, cart, item_id, data):
        items = cart['items']
        item = next(filter_result('item_id', item_id, items), None)
        if item is None:
            return item
        item['quantity'] += data['quantity']
        return cart

    def remove_item(self, cart, item_id):
        items = cart['items']
        item = next(filter_result('item_id', item_id, items), None)
        if item is None:
            return item
        items.remove(item)
        return cart

    def count_all_items(self, order):
        count = 0
        items = order["items"]
        for item in items:
            count += item["quantity"]
        return count

    def get_sub_total(self, cart):
        sub_total = 0
        items = cart["items"]
        for item in items:
            sub_total += (item["price"] * item["quantity"])
        return sub_total

    def get_tax_amount(self, cart):
        return cart["sub_total"] * cart["tax_rate"]

    def get_total(self, cart):
        sub_total = cart["sub_total"]
        return sub_total + cart["shipping_fee"] + cart["tax_amount"]

    def get_feed(self, carts):
        for cart in carts:
            cart["sub_total"] = self.get_sub_total(cart)
            cart["tax_amount"] = self.get_tax_amount(cart)
            cart["number_of_items"] = self.count_all_items(cart)
            cart["total"] = self.get_total(cart)
        return carts
