from helpers.Helper import get_json
from models.v1.Cart import Cart

from os import path
import sys
import json

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Cart()


class CartController_v1(Resource):
    def get(self, customer_id):
        cart = model.find_by_customer(customer_id)
        if cart is None:
            return {"message": "Customer not found"}, 404
        return get_json(cart), 200

    def post(self, customer_id):
        new_cart = Cart(customer_id, []).__dict__
        cart = model.find_by_customer(customer_id)
        if cart is None:
            model.add(new_cart)
            return get_json(new_cart), 201
        return {"message": "Cart already exists for user"}, 400

    def put(self, customer_id):
        data = request.get_json()
        cart = model.add_item(customer_id, data)
        if cart is None:
            return {"message": "Failed to add item to cart"}, 400
        return get_json(cart), 200


class ItemController_v1(Resource):
    def put(self, customer_id, item_id):
        data = request.get_json()
        item = model.edit_item(customer_id, item_id, data)
        if item is None:
            return {"message": "Failed to edit item from cart"}, 400
        return get_json(item), 200

    def delete(self, customer_id, item_id):
        cart = model.remove_item(customer_id, item_id)
        if cart is None:
            return {"message": "Failed to remove item from cart"}, 400
        return get_json(cart), 200
