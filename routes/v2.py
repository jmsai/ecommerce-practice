from controllers.v2.SignupController import SignupController
from controllers.v2.LoginController import LoginController
from controllers.v2.CustomerController import CustomerController
from controllers.v2.ProductController import ProductController
from controllers.v2.ProductDetailsController import ProductDetailsController
from controllers.v2.CartController import CartController
from controllers.v2.ItemController import ItemController
from controllers.v2.OrderController import OrderController
from controllers.v2.OrderDetailsController import OrderDetailsController

from flask import Blueprint
from flask_restful import Api
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

api_v2 = Blueprint('api_v2', __name__)
api = Api(api_v2)


PRODUCTS_ROUTE = '/products'
CUSTOMERS_ROUTE = '/customers'
CARTS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/carts'
ITEMS_ROUTE = f'{CARTS_ROUTE}/<cart_id>/items'
ORDERS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/orders'

# Customer Routes
api.add_resource(SignupController, '/signup')
api.add_resource(LoginController, '/login')
api.add_resource(CustomerController, f'{CUSTOMERS_ROUTE}/<_id>')

# Product Routes
api.add_resource(ProductController, '/', f'{PRODUCTS_ROUTE}')
api.add_resource(ProductDetailsController, f'{PRODUCTS_ROUTE}/<_id>')

# Cart Routes
api.add_resource(CartController, f'{CARTS_ROUTE}')
api.add_resource(ItemController, f'{ITEMS_ROUTE}/<item_id>')

# Order Routes
api.add_resource(OrderController, f'{ORDERS_ROUTE}')
api.add_resource(OrderDetailsController, f'{ORDERS_ROUTE}/<order_id>')
