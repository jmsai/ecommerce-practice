from controllers.v1.Product import Product

import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class ProductModel(Product):
    def find_all(self):
        with open("seedv2.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["products"]
