from controllers.v1.Customer import SignupController_v1
from controllers.v1.Customer import LoginController_v1
from controllers.v1.Customer import CustomerController_v1
from controllers.v1.Product import ProductListController_v1
from controllers.v1.Product import ProductController_v1
from controllers.v1.Cart import CartController_v1
from controllers.v1.Cart import ItemController_v1
from controllers.v1.Order import OrderListController_v1
from controllers.v1.Order import OrderController_v1

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

API_VERSION = '/api/v1'
CUSTOMERS_ROUTE = f'{API_VERSION}/customers/<customer_id>'
PRODUCTS_ROUTE = f'{API_VERSION}/products'
CARTS_ROUTE = f'{CUSTOMERS_ROUTE}/cart/items'
ORDERS_ROUTE = f'{CUSTOMERS_ROUTE}/orders'


def get_from(api):
    # Customer Routes
    api.add_resource(SignupController_v1, f'{API_VERSION}/signup')
    api.add_resource(LoginController_v1, f'{API_VERSION}/login')
    api.add_resource(CustomerController_v1, f'{CUSTOMERS_ROUTE}')

    # Product Routes
    api.add_resource(ProductListController_v1, f'{PRODUCTS_ROUTE}/')
    api.add_resource(ProductController_v1, f'{PRODUCTS_ROUTE}/<product_id>')

    # Cart Route
    api.add_resource(CartController_v1, f'{CARTS_ROUTE}')
    api.add_resource(ItemController_v1, f'{CARTS_ROUTE}/<item_id>')

    # Order Route
    api.add_resource(OrderListController_v1, f'{ORDERS_ROUTE}')
    api.add_resource(OrderController_v1, f'{ORDERS_ROUTE}/<order_id>')
