import json
import uuid
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class Order:
    def __init__(self, order_id='', tracking_id='', delivery_date='',
                 delivery_status='', shipping_fee='', shipping_address='',
                 billing_address='', transaction_date='', payment_status='',
                 payment_method='', payment_total='', tax_amount='',
                 discount_total='', items='', customer_id=''):
        self.order_id = order_id
        self.tracking_id = tracking_id
        self.delivery_date = delivery_date
        self.delivery_status = delivery_status
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.transaction_date = transaction_date
        self.payment_status = payment_status
        self.payment_method = payment_method
        self.tax_amount = tax_amount
        self.shipping_fee = shipping_fee
        self.discount_total = discount_total
        self.payment_total = payment_total
        self.items = items
        self.customer_id = customer_id

    def find_all_orders(self):
        with open('seed.json', 'r') as seed_file:
            data = json.load(seed_file)
            return data["orders"]

    def find_orders_by_customer(self, customer_id):
        orders = self.find_all_orders()
        customer_orders = list(filter(lambda data: data['customer_id'] == customer_id, orders))
        return customer_orders

    def search_order_by_id(self, customer_id, order_id):
        customer_orders = self.find_orders_by_customer(customer_id)
        order = next(filter(lambda data: data['order_id'] == order_id, customer_orders), None)
        return order

    def find_order_by_id(self, order_id):
        orders = self.find_all_orders()
        order = next(filter(lambda data: data['order_id'] == order_id, orders), None)
        return order

    def add_order(self, customer_id, request_data):
        customer = self.find_orders_by_customer(customer_id)
        customer.append(request_data)
        return customer

    def edit_order(self, order_id, request_data):
        orders = self.find_all_orders()
        order = next(filter(lambda data: data['order_id'] == order_id, orders), None)
        if order is None:
            orders.append(request_data)
        else:
            order.update(request_data)
        return orders
