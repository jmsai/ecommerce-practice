from api.v1.common import get_response
from api.v1.models.Product import Product
from api.v1.views.ProductView import ProductView
from error.model import NotFoundError
from error.model import BadRequestError
from error.model import UnprocessableEntityError
from error.model import ResourceAlreadyExistError
from error.view import ErrorView

from flask import request
from flask_restful import Resource

model = Product()
view = ProductView()
ErrorView = ErrorView()


class ProductController(Resource):
    def get(self):
            products = model.find_all()

            if products is None:
                error = NotFoundError("Results")
                display = ErrorView.display(error)
                return get_response(display, 404)

            product_name = request.args.get('name')

            if product_name is None:
                feed = model.get_feed(products)
                display = view.display_list(feed)
                return get_response(display, 200)

            product = model.find_by_name(products, product_name)

            if product is None:
                error = NotFoundError("Product")
                display = ErrorView.display(error)
                return get_response(display, 404)

            original_price = product["original_price"]
            discount_rate = product["discount_rate"]
            product["price"] = model.get_price(discount_rate, original_price)

            display = view.display_details(product)
            return get_response(display, 200)


class ProductDetailsController(Resource):
    def get(self, _id):
        products = model.find_all()

        if products is None:
            error = NotFoundError("Results")
            display = ErrorView.display(error)
            return get_response(display, 404)

        product = model.find_by(products, _id)

        if product is None:
            error = NotFoundError("Product")
            display = ErrorView.display(error)
            return get_response(display, 404)

        original_price = product["original_price"]
        discount_rate = product["discount_rate"]
        product["price"] = model.get_price(discount_rate, original_price)

        display = view.display_details(product)
        return get_response(display, 200)
