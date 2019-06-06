from helpers.Helper import get_json
from models.v1.Product import Product

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Product()


class ProductListController_v1(Resource):
    def get(self):
        product_name = request.args.get('name')
        products = model.find_all()
        if product_name is None:
            return get_json(products), 200
        product = model.find_by_name(products, product_name)
        if product is None:
            return {"message": "No results found"}, 404
        return get_json(product), 200


class ProductController_v1(Resource):
    def get(self, _id):
        products = model.find_all()
        product = model.find_by(products, _id)
        if product is None:
            return {"message": "No product found"}, 404
        return get_json(product), 200
