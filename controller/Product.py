from model.Product import Product

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Product()


class ProductListController(Resource):
    def get(self):
        product_id = request.args.get('id')
        if product_id is None:
            products = model.find_all_products()
            return products, 200
        else:
            product = model.find_product_by_id(product_id)
            if product is None:
                return {"message": "No results found"}, 404
            else:
                return product, 200


class ProductController(Resource):
    def get(self, product_id):
        product = model.find_product_by_id(product_id)
        if product is None:
            return {"message": "No product found"}, 404
        else:
            return product, 200
