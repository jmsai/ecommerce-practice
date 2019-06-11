from api.v2.models.ProductModel import ProductModel
from api.v2.views.ProductView import ProductView
from api.v2.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

Product = ProductModel()
ProductView = ProductView()
Error = ErrorView()


class ProductController(Resource):
    def get(self):
            product_name = request.args.get('name')
            products = Product.find_all()

            if products is None:
                return Error.no_results_found(), 404

            if product_name is None:
                feed = Product.get_feed(products)
                return ProductView.display_list(feed), 200

            product = Product.find_by_name(products, product_name)

            discount_rate = product["discount_rate"]
            product["discount"] = Product.get_percentage(discount_rate)

            original_price = product["original_price"]
            product["price"] = Product.get_price(discount_rate, original_price)

            return ProductView.display_details(product), 200
