import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_sku
import db

class Product:
    def __init__(self, name, product_type, original_price, discount_rate, seller_sku, images = None, inside_box = '', description = '', brand = '', model = '', warranty_period = '', warranty_type = ''):
        self.sku = generate_sku()
        self.name = name
        self.images = images
        self.product_type = product_type
        self.description = description
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period
        self.warranty_type = warranty_type
        self.inside_box = inside_box
        self.original_price = original_price
        self.discount_rate = discount_rate
        self.discount_price = original_price - (original_price * (discount_rate / 100))
        self.seller_sku = seller_sku

    def display_json(self):
        product = {
            "sku": self.sku,
            "name": self.name,
            "images": self.images,
            "product_type": self.product_type,
            "description": self.description,
            "brand": self.brand,
            "model": self.model,
            "warranty_period": self.warranty_period,
            "warranty_type": self.warranty_type,
            "inside_box": self.inside_box,
            "original_price": self.original_price,
            "discount_price": self.discount_price,
            "seller_sku": self.seller_sku
        }
        return convert_to_json(product)