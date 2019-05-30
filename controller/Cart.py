from model.Cart import Cart

from os import path
import sys
import json

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Cart()


class CartController(Resource):
    def get(self, customer_id):
        cart = model.find_cart_by_customer_id(customer_id)
        if cart is None:
            return {"message": "Customer not found"}, 404
        else:
            return cart, 200

    def post(self, customer_id):
        new_cart = Cart(customer_id, [], 0).__dict__
        cart = model.find_cart_by_customer_id(customer_id)
        if cart is None:
            model.create_cart_for_user(new_cart)
            return new_cart, 201
        else:
            return {"message": "Cart already exists for user"}, 400

    def put(self, customer_id):
        data = request.get_json()
        cart = model.add_item_to_cart(customer_id, data) 
        if cart is None:
            return {"message": "Failed to add item to cart"}, 400
        else:
            return cart, 200


class ItemController(Resource):
    def put(self, customer_id, item_id):
        data = request.get_json()
        item = model.edit_item_from_cart(customer_id, item_id, data)
        if item is None:
            return {"message": "Failed to edit item from cart"}, 400
        else:
            return item, 200

    def delete(self, customer_id, item_id):
        cart = model.remove_item_from_cart(customer_id, item_id)
        if cart is None:
            return {"message": "Failed to remove item from cart"}, 400
        else:
            return cart, 200
