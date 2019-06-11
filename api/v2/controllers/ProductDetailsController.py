from api.v2.models.ProductModel import ProductModel
from api.v2.views.ErrorView import ErrorView
from api.v2.views.ProductView import ProductView

from flask import request
from flask_restful import Resource

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
