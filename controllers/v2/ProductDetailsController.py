from helpers.Helper import get_json
from models.v2.ProductModel import ProductModel
from views.ErrorView import ErrorView
from views.v2.ProductView import ProductView

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()
ProductView = ProductView()
Error = ErrorView()


class ProductDetailsController(Resource):
    def get(self, _id):
        products = Product.find_all()
        product = Product.find_by(products, _id)

        if product is None:
            return Error.product_not_found(), 404

        discount_rate = product["discount_rate"]
        product["discount"] = Product.get_percentage(discount_rate)

        original_price = product["original_price"]
        product["price"] = Product.get_price(discount_rate, original_price)

        return ProductView.display_details(product), 200

    # def get(self, _name=None):
    #     products = Product.find_all()
    #     product = Product.find_by(products, _name)

    #     if product is None:
    #         return Error.product_not_found(), 404

    #     discount_rate = product["discount_rate"]
    #     product["discount"] = Product.get_percentage(discount_rate)

    #     original_price = product["original_price"]
    #     product["price"] = Product.get_price(discount_rate, original_price)

    #     return ProductView.display_details(product), 200
