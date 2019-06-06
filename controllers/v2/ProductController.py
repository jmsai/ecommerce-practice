from helpers.Helper import get_json
from models.v2.ProductModel import ProductModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()


class ProductController_v2(Resource):
    def get(self, _id):
        products = Product.find_all()
        product = Product.find_by(products, _id)
        if product is None:
            return {"message": "No product found"}, 404
        return get_json(product), 200
