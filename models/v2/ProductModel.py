from helpers.FilterHelper import filter_result

import json
import uuid
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class ProductModel:
    def find_all(self):
        with open("seedv2.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["products"]

    def find_by(self, _id):
        products = self.find_all()
        product = filter_result('product_id', _id, products)
        return next(product, None)

    def find_by_name(self, _name):
        products = self.find_all()
        product_name = _name.replace('_', ' ')
        product = filter_result('name', product_name, products)
        return next(product, None)
