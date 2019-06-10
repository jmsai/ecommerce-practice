from helpers.Helper import get_json
from models.v2.ProductModel import ProductModel
from views.v2.ProductView import ProductView
from views.ErrorView import ErrorView

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Product = ProductModel()
ProductView = ProductView()
Error = ErrorView()


class ProductController(Resource):
    def get(self):
        product_name = request.args.get('name')
        products = Product.find_all()

        if product_name is None:
            feed = Product.get_feed(products)
            return ProductView.display_list(feed), 200

        product = Product.find_by_name(products, product_name)

        if product is None:
            return Error.no_results_found(), 404

        discount_rate = product["discount_rate"]
        product["discount"] = Product.get_percentage(discount_rate)

        original_price = product["original_price"]
        product["price"] = Product.get_price(discount_rate, original_price)

        return ProductView.display_details(product), 200
