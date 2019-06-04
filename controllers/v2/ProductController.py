from helpers.v2.JSONHelper import get_json
from models.v2.ProductModel import ProductModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()


class ProductController_v2(Resource):
    def get(self, _id):
        product = Product.find_by(_id)
        if product is None:
            return {"message": "No product found"}, 404
        else:
            return get_json(product), 200
