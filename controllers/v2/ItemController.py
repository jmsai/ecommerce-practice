from models.v2.CartModel import CartModel
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


class ItemController(Resource):
    def put(self, cart_id, customer_id, item_id):
        data = request.get_json()
        cart = Cart.find_by_customer(customer_id)
        item = Cart.edit_item(cart, item_id, data)

        if item is None:
            return Error.item_not_found(), 404

        sub_total = Cart.get_sub_total(cart)
        print(sub_total)
        return CartView.display_cart(cart), 200

    def delete(self, cart_id, customer_id, item_id):
        cart = Cart.find_by_customer(customer_id)
        item = Cart.remove_item(cart, item_id)

        if item is None:
            return Error.item_not_found(), 404

        return CartView.display_cart(cart), 200
