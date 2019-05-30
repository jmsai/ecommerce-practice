from helper.Helper import filter_result

import json
import uuid
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class Product:
    def __init__(self, _id='', name='', product_type='', original_price='',
                 discount_rate='', images=None, inside_box='',
                 description='', brand='', model='',
                 warranty_period='', warranty_type=''):
        self.product_id = _id
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

    def find_all_products(self):
        with open("seed.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["products"]

    def find_product_by_id(self, _id):
        products = self.find_all_products()
        product = filter_result('product_id', _id, products)
        return next(product, None)
