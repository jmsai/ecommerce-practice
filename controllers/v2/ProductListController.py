from helpers.JSONHelper import get_json
from models.ProductModel import ProductModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()


class ProductListController(Resource):
    def get(self):
        product_name = request.args.get('name')
        if product_name is None:
            products = Product.find_all()
            return get_json(products), 200
        else:
            product = Product.find_by_name(product_name)
            if product is None:
                return {"message": "No results found"}, 404
            else:
                return get_json(product), 200
