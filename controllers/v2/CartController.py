from models.CartModel import CartModel

from os import path
import sys
import json

from flask import request, jsonify
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Cart = CartModel()


class CartController(Resource):
    def get(self, customer_id):
        cart = Cart.find_by_customer(customer_id)
        if cart is None:
            return {"message": "Customer not found"}, 404
        return jsonify(cart), 200

    def post(self, customer_id):
        new_cart = CartModel(customer_id, [], 0).__dict__
        cart = Cart.find_by_customer(customer_id)
        if cart is None:
            Cart.add(new_cart)
            return new_cart, 201
        return {"message": "Cart already exists for user"}, 400

    def put(self, customer_id):
        data = request.get_json()
        cart = Cart.add_item(customer_id, data)
        if cart is None:
            return {"message": "Failed to add item to cart"}, 400
        return jsonify(cart), 200
