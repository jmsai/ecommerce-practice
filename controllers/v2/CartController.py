from helpers.Helper import get_json
from models.v2.CartModel import CartModel
from controllers.v1.Cart import CartController_v1

from os import path
import sys

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Cart = CartModel()


class CartController_v2(CartController_v1):
    def post(self, customer_id):
        new_cart = CartModel(customer_id, []).__dict__
        cart = Cart.find_by_customer(customer_id)
        if cart is None:
            Cart.add(new_cart)
            return get_json(new_cart), 201
        return {"message": "Cart already exists for user"}, 400
