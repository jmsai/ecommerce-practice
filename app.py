from controller.Product import ProductController, ProductListController
from controller.Customer import CustomerController, SignupController
from controller.Customer import LoginController
from controller.Cart import CartController, ItemController
from controller.Order import OrderController, OrderListController

from flask import Flask, request
from flask_restful import Resource, Api
import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

app = Flask(__name__)
api = Api(app)

# User Routes
api.add_resource(SignupController,
                 '/api/v1/signup')
api.add_resource(LoginController,
                 '/api/v1/login')
api.add_resource(CustomerController,
                 '/api/v1/customers/<customer_id>')

# Product Routes
api.add_resource(ProductListController,
                 '/api/v1/')
api.add_resource(ProductController,
                 '/api/v1/products/<product_id>')

# Cart Route
api.add_resource(CartController,
                 '/api/v1/customers/<customer_id>/cart/items')
api.add_resource(ItemController,
                 '/api/v1/customers/<customer_id>/cart/items/<item_id>')

# Order Route
api.add_resource(OrderListController,
                 '/api/v1/customers/<customer_id>/orders')
api.add_resource(OrderController,
                 '/api/v1/customers/<customer_id>/orders/<order_id>')


# Error Page Route
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()

app.run(port=3000)
