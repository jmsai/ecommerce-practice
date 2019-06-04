from helper.Helper import filter_result

import json
import uuid
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class Product:
    def find_all_products(self):
        with open("seed.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["products"]

    def find_product_by_id(self, _id):
        products = self.find_all_products()
        product = filter_result('product_id', _id, products)
        return next(product, None)

    def find_product_by_name(self, name):
        products = self.find_all_products()
        product_name = name.replace('_', ' ')
        product = filter_result('name', product_name, products)
        return next(product, None)
