from helpers.v2.JSONHelper import get_json
from models.v2.CartModel import CartModel

from os import path
import sys
import json

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Cart = CartModel()


class ItemController_v2(Resource):
    def put(self, customer_id, item_id):
        data = request.get_json()
        items = Cart.find_all_items(customer_id)
        item = Cart.edit_item(items, item_id, data)
        if item is None:
            return {"message": "Failed to edit item from cart"}, 400
        return get_json(item), 200

    def delete(self, customer_id, item_id):
        items = Cart.find_all_items(customer_id)
        cart = Cart.remove_item(items, item_id)
        if cart is None:
            return {"message": "Failed to remove item from cart"}, 400
        return get_json(cart), 200
