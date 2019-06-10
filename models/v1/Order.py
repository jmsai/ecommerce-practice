from helpers.Helper import filter_result
from helpers.Helper import generate_id
from helpers.Helper import generate_tracking_number

import datetime as Date
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
orders = []


class Order:
    def __init__(self, customer_name='', phone_number='', shipping_address='',
                 billing_address='', delivery_date='', payment_method='',
                 payment_date='', shipping_fee='', tax_rate='',
                 items='', customer_id=''):
        self.order_id = generate_id()
        self.transaction_date = f'{Date.datetime.now()}'
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.tracking_id = generate_tracking_number()
        self.delivery_status = "Pending"
        self.delivery_date = delivery_date
        self.payment_date = payment_date
        self.payment_status = "Pending"
        self.payment_method = payment_method
        self.shipping_fee = shipping_fee
        self.tax_rate = tax_rate
        self.items = items
        self.customer_id = customer_id

    def find_all(self):
        return orders

    def find_by_customer(self, _id):
        orders = self.find_all()
        customer_orders = filter_result('customer_id', _id, orders)
        return list(customer_orders)

    def search_by(self, customer_id, order_id):
        customer_orders = self.find_by_customer(customer_id)
        order = filter_result('order_id', order_id, customer_orders)
        return next(order, None)

    def find_by(self, _id):
        orders = self.find_all()
        order = filter_result('order_id', _id, orders)
        return next(order, None)

    def add(self, new_order):
        orders.append(new_order)

    def edit(self, customer_id, order_id, data):
        orders = self.find_by_customer(customer_id)

        if not orders:
            return orders

        order = next(filter_result('order_id', order_id, orders), None)

        if order is None:
            return order

        order.update(data)

        return order

    def count_all_items(self, order):
        count = 0
        items = order["items"]
        for item in items:
            count += item["quantity"]
        return count

    def get_sub_total(self, order):
        sub_total = 0
        items = order["items"]
        for item in items:
            sub_total += (item["price"] * item["quantity"])
        return sub_total

    def get_tax_amount(self, order):
        return order["sub_total"] * order["tax_rate"]

    def get_total(self, order):
        sub_total = order["sub_total"]
        return sub_total + order["shipping_fee"] + order["tax_amount"]

    def get_feed(self, orders):
        for order in orders:
            order["sub_total"] = self.get_sub_total(order)
            order["tax_amount"] = self.get_tax_amount(order)
            order["number_of_items"] = self.count_all_items(order)
            order["total"] = self.get_total(order)

        return orders
