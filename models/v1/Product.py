from helpers.Helper import filter_result

import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class Product:
    def find_all(self):
        with open("seedv1.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["products"]

    def find_by(self, products, _id):
        product = filter_result('product_id', _id, products)
        return next(product, None)

    def find_by_name(self,  products, _name):
        product_name = _name.replace('_', ' ')
        product = filter_result('name', product_name, products)
        return next(product, None)
