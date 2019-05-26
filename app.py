from flask import Flask, request
from flask_restful import Resource, Api
import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from  controller.Product import ProductController, ProductListController
from controller.Customer import CustomerController, SignupController, LoginController
from controller.Cart import CartController
from controller.Order import OrderController, OrderListController

app = Flask(__name__)
api = Api(app)

# User Routes
api.add_resource(SignupController, '/signup')
api.add_resource(LoginController, '/login')
api.add_resource(CustomerController, '/<customer_id>')

# Product Routes
api.add_resource(ProductListController, '/')
api.add_resource(ProductController, '/product/<_id>')

# Cart Route
api.add_resource(CartController, '/<customer_id>/cart')

# Order Route
api.add_resource(OrderListController, '/<customer_id>/orders')
api.add_resource(OrderController, '/order/<order_id>')

# Error Page Route
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()

app.run(port=3000)