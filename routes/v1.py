from controllers.v1.Customer import SignupController
from controllers.v1.Customer import LoginController
from controllers.v1.Customer import CustomerController
from controllers.v1.Product import ProductController
from controllers.v1.Product import ProductDetailsController
from controllers.v1.Cart import CartController
from controllers.v1.Cart import ItemController
from controllers.v1.Order import OrderController
from controllers.v1.Order import OrderDetailsController

from flask import Blueprint
from flask_restful import Api
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)

CUSTOMERS_ROUTE = '/customers'
PRODUCTS_ROUTE = '/products'
CARTS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/items'
ORDERS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/orders'

# Customer Routes
api.add_resource(SignupController, '/signup')
api.add_resource(LoginController, '/login')
api.add_resource(CustomerController, f'{CUSTOMERS_ROUTE}/<_id>')

# Product Routes
api.add_resource(ProductController, '/', f'{PRODUCTS_ROUTE}')
api.add_resource(ProductDetailsController, f'{PRODUCTS_ROUTE}/<_id>')

# Cart Route
api.add_resource(CartController, f'{CARTS_ROUTE}')
api.add_resource(ItemController, f'{CARTS_ROUTE}/<item_id>')

# Order Route
api.add_resource(OrderController, f'{ORDERS_ROUTE}')
api.add_resource(OrderDetailsController, f'{ORDERS_ROUTE}/<order_id>')
