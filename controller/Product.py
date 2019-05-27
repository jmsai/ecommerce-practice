from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask_restful import Resource

from model.Product import Product

model = Product()

class ProductListController(Resource):
    def get(self):
        products = model.find_all_products()
        if products is None:
            return { "message": "No products available" }, 404
        else:
            return products, 200

class ProductController(Resource):
    def get(self, _id):
        product = model.find_product_by_id(_id)
        if product is None:
            return { "message": "No product found" }, 404
        else:
            return product, 200