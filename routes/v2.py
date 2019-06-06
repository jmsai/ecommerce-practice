from controllers.v2.SignupController import SignupController_v2
from controllers.v2.LoginController import LoginController_v2
from controllers.v2.CustomerController import CustomerController_v2
from controllers.v2.ProductListController import ProductListController_v2
from controllers.v2.ProductController import ProductController_v2
from controllers.v2.ReviewListController import ReviewListController
from controllers.v2.CartController import CartController_v2
from controllers.v2.ItemController import ItemController_v2
from controllers.v2.OrderListController import OrderListController_v2
from controllers.v2.OrderController import OrderController_v2

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

API_VERSION = '/api/v2'
PRODUCTS_ROUTE = f'{API_VERSION}/products'
CUSTOMERS_ROUTE = f'{API_VERSION}/customers'
CARTS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/carts'
ITEMS_ROUTE = f'{CARTS_ROUTE}/<cart_id>/items'
ORDERS_ROUTE = f'{CUSTOMERS_ROUTE}/<customer_id>/orders'
REVIEWS_ROUTE = f'{PRODUCTS_ROUTE}/<product_id>/reviews'


def get_from(api):
    # Customer Routes
    api.add_resource(SignupController_v2, f'{API_VERSION}/signup')
    api.add_resource(LoginController_v2, f'{API_VERSION}/login')
    api.add_resource(CustomerController_v2, f'{CUSTOMERS_ROUTE}/<_id>')

    # Product Routes
    api.add_resource(ProductListController_v2, f'{API_VERSION}/')
    api.add_resource(ProductController_v2, f'{PRODUCTS_ROUTE}/<_id>')
    api.add_resource(ReviewListController, f'{REVIEWS_ROUTE}')

    # Cart Routes
    api.add_resource(CartController_v2, f'{CARTS_ROUTE}')
    api.add_resource(ItemController_v2, f'{ITEMS_ROUTE}/<item_id>')

    # Order Routes
    api.add_resource(OrderListController_v2, f'{ORDERS_ROUTE}')
    api.add_resource(OrderController_v2, f'{ORDERS_ROUTE}/<order_id>')
