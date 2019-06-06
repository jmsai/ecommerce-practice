from helpers.Helper import filter_result
from helpers.Helper import generate_id
from helpers.Helper import generate_tracking_number

import datetime as Date
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
orders = []


class Order:
    __discount_total = 0
    __payment_total = 0
    __tax_amount = 0

    def __init__(self, delivery_date='', shipping_address='',
                 billing_address='', payment_method='',
                 shipping_fee='', items='', customer_id=''):
        self.order_id = generate_id()
        self.tracking_id = generate_tracking_number()
        self.transaction_date = f'{Date.datetime.now()}'
        self.payment_status = "Pending"
        self.delivery_status = "Pending"
        self.delivery_date = delivery_date
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.payment_method = payment_method
        self.shipping_fee = shipping_fee
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
