from models.v2.CartModel import CartModel
from helpers.Helper import get_json

from os import path
import sys

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Cart = CartModel()


class ItemController_v2(Resource):
    def put(self, cart_id, customer_id, item_id):
        data = request.get_json()
        item = Cart.edit_item(customer_id, item_id, data)
        if item is None:
            return {"message": "Item is not found"}, 404
        return get_json(item), 200

    def delete(self, cart_id, customer_id, item_id):
        cart = Cart.remove_item(customer_id, item_id)
        if cart is None:
            return {"message": "Item is not found"}, 404
        return get_json(cart), 200
