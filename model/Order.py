from helper.Helper import filter_result, generate_id
from helper.Helper import generate_tracking_number

import json
import uuid
import datetime as Date
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
orders = []


class Order:
    def __init__(self, delivery_date='', shipping_address='',
                 billing_address='', payment_method='', tax_amount='',
                 shipping_fee='', discount_total='', payment_total='',
                 items='', customer_id=''):
        self.order_id = generate_id()
        self.tracking_id = generate_tracking_number()
        self.delivery_date = delivery_date
        self.delivery_status = "Pending"
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.transaction_date = f'{Date.datetime.now()}'
        self.payment_status = "Pending"
        self.payment_method = payment_method
        self.tax_amount = tax_amount
        self.shipping_fee = shipping_fee
        self.discount_total = discount_total
        self.payment_total = payment_total
        self.items = items
        self.customer_id = customer_id

    def find_all_orders(self):
        return orders

    def find_orders_by_customer(self, customer_id):
        orders = self.find_all_orders()
        customer_orders = filter_result('customer_id', customer_id, orders)
        return list(customer_orders)

    def search_order_by_id(self, customer_id, order_id):
        customer_orders = self.find_orders_by_customer(customer_id)
        order = filter_result('order_id', order_id, customer_orders)
        return next(order, None)

    def find_order_by_id(self, order_id):
        orders = self.find_all_orders()
        order = filter_result('order_id', order_id, orders)
        return next(order, None)

    def add_order(self, new_order):
        orders.append(new_order)

    def edit_order(self, customer_id, order_id, data):
        orders = self.find_orders_by_customer(customer_id)
        order = next(filter_result('order_id', order_id, orders), None)
        if order is None:
            orders.append(data)
        else:
            order.update(data)
        return orders
