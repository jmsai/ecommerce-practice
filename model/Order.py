import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_sku, generate_tracking_number

class Order:
    def __init__(self, transaction_date, delivery_time, customer_id, shipping_fee, shipping_address, billing_address, payment_method, grand_total, tax_amount, discount_total, items):
        self.order_number = generate_sku()
        self.tracking_id = generate_tracking_number()
        self.transaction_date = transaction_date
        self.delivery_time = delivery_time
        self.customer_id = customer_id
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.payment_method = payment_method
        self.tax_amount = tax_amount
        self.shipping_fee = shipping_fee
        self.discount_total = discount_total
        self.grand_total = grand_total
        self.items = items

    def display_json(self):
        order = {
            "order_numer": self.order_number,
            "tracking_id": self.tracking_id,
            "transaction_date": self.transaction_date,
            "delivery_time": self.delivery_time,
            "customer_id": self.customer_id,
            "shipping_address": self.shipping_address,
            "billing_address": self.billing_address,
            "payment_method": self.payment_method,
            "tax_amount": self.tax_amount,
            "shipping_fee": self.shipping_fee,
            "discount_total": self.discount_total,
            "grand_total": self.grand_total,
            "items": self.items            
        }
        return convert_to_json(order)