from helpers.Helper import get_json
from models.v1.Product import Product
from views.v1.ProductView import ProductView
from views.ErrorView import ErrorView

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Product()
view = ProductView()
Error = ErrorView()


class ProductController(Resource):
    def get(self):
        product_name = request.args.get('name')
        products = model.find_all()

        if product_name is None:
            feed = model.get_feed(products)
            return view.display_list(feed), 200

        product = model.find_by_name(products, product_name)

        if product is None:
            return Error.no_results_found(), 404

        original_price = product["original_price"]
        discount_rate = product["discount_rate"]
        product["price"] = model.get_price(discount_rate, original_price)
        
        return view.display_details(product), 200


class ProductDetailsController(Resource):
    def get(self, _id):
        products = model.find_all()
        product = model.find_by(products, _id)

        if product is None:
            return Error.product_not_found(), 404

        original_price = product["original_price"]
        discount_rate = product["discount_rate"]
        product["price"] = model.get_price(discount_rate, original_price)

        return view.display_details(product), 200
