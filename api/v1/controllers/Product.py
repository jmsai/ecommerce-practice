from api.v1.models.Product import Product
from api.v1.views.ProductView import ProductView
from api.v1.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

model = Product()
view = ProductView()
Error = ErrorView()


class ProductController(Resource):
    def get(self):
        try:
            product_name = request.args.get('name')
            products = model.find_all()

            if product_name is None:
                feed = model.get_feed(products)
                return view.display_list(feed), 200

            product = model.find_by_name(products, product_name)

            original_price = product["original_price"]
            discount_rate = product["discount_rate"]
            product["price"] = model.get_price(discount_rate, original_price)

            return view.display_details(product), 200

        except:
            return Error.no_results_found(), 404


class ProductDetailsController(Resource):
    def get(self, _id):
        try:
            products = model.find_all()
            product = model.find_by(products, _id)

            original_price = product["original_price"]
            discount_rate = product["discount_rate"]
            product["price"] = model.get_price(discount_rate, original_price)

            return view.display_details(product), 200

        except:
            return Error.product_not_found(), 404
