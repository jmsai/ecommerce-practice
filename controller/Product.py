from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask_restful import Resource

from model.Product import Product
import view.Product as view

model = Product()

class ProductListController(Resource):
    def get(self):
        products = model.find_all_products()
        return products, 200 if products else 404

class ProductController(Resource):
    def get(self, _id):
        product = model.find_product_by_id(_id)
        return product, 200 if product else 404