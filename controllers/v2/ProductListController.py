from helpers.Helper import get_json
from models.v2.ProductModel import ProductModel
from controllers.v1.Product import ProductListController_v1

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()


class ProductListController_v2(Resource):
    def get(self):
        product_name = request.args.get('name')
        products = Product.find_all()
        if product_name is None:
            return get_json(products), 200
        product = Product.find_by_name(products, product_name)
        if product is None:
            return {"message": "No results found"}, 404
        return get_json(product), 200
