import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_sku

class Product:
    def __init__(self, name, product_type, original_price, discount_rate, 
                 images = None, inside_box = '', description = '', brand = '', 
                 model = '', warranty_period = '', warranty_type = ''):
        self.product_id = generate_sku()
        self.name = name
        self.description = description
        self.product_type = product_type
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period
        self.warranty_type = warranty_type
        self.inside_box = inside_box
        self.images = images
        self.original_price = original_price
        self.discount_rate = discount_rate

    def get_discount_price(self):
        return self.original_price - (self.original_price * (self.discount_rate / 100))

