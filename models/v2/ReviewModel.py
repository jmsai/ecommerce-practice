from helpers.v2.FilterHelper import filter_result

from os import path
import sys
import json

sys.path.append(path.join(path.dirname(__file__), '..'))


class ReviewModel:
    def find_all(self):
        with open("seedv2.json", "r") as seed_file:
            data = json.load(seed_file)
            return data["reviews"]   

    def find_by_product(self, product_id):
        reviews = self.find_all()
        review = filter_result('product_id', product_id, reviews)
        return next(review, None)
