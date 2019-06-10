from helpers.Helper import get_json
from models.v2.CartModel import CartModel
from controllers.v1.Cart import CartController as CartController_v1
from views.v2.CartView import CartView
from views.v2.ErrorView import ErrorView

from os import path
import sys

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Cart = CartModel()
CartView = CartView()
Error = ErrorView()


class CartController(CartController_v1):
    def post(self, customer_id):
        new_cart = CartModel(customer_id, []).__dict__
        cart = Cart.find_by_customer(customer_id)

        if cart is not None:
            return Error.cart_already_exist(), 400

        Cart.add(new_cart)

        return new_cart, 201
