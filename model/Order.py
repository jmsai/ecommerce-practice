import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_sku, generate_tracking_number

class Order:
    def __init__(self, delivery_date, delivery_status, shipping_fee, 
                 shipping_address, billing_address, transaction_date, 
                 payment_status, payment_method, payment_total, tax_amount, 
                 discount_total, items, customer_id):
        self.order_id = generate_sku()
        self.tracking_id = generate_tracking_number()
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