from controllers.v1.Customer import SignupController_v1
from controllers.v1.Customer import LoginController
from controllers.v1.Customer import CustomerController
from controllers.v1.Product import ProductController
from controllers.v1.Product import ProductDetailsController
from controllers.v1.Cart import CartController
from controllers.v1.Cart import ItemController
from controllers.v1.Order import OrderController
from controllers.v1.Order import OrderDetailsController

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


def get_from(api):
    API_VERSION = '/api/v1'
    CUSTOMERS_ROUTE = f'{API_VERSION}/customers'
    PRODUCTS_ROUTE = f'{API_VERSION}/products'
    CARTS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/items'
    ORDERS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/orders'

    # Customer Routes
    api.add_resource(SignupController_v1, f'{API_VERSION}/signup')
    api.add_resource(LoginController, f'{API_VERSION}/login')
    api.add_resource(CustomerController, f'{CUSTOMERS_ROUTE}/<_id>')

    # Product Routes
    api.add_resource(ProductController, f'{API_VERSION}/')
    api.add_resource(ProductDetailsController, f'{PRODUCTS_ROUTE}/<_id>')

    # Cart Route
    api.add_resource(CartController, f'{CARTS_ROUTE}')
    api.add_resource(ItemController, f'{CARTS_ROUTE}/<item_id>')

    # Order Route
    api.add_resource(OrderController, f'{ORDERS_ROUTE}')
    api.add_resource(OrderDetailsController, f'{ORDERS_ROUTE}/<order_id>')
