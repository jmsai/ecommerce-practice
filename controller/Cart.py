from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask import request
from flask_restful import Resource

from model.Cart import Cart
import view.Cart as view

model = Cart()

class CartController(Resource):
    def get(self, customer_id):
        cart = model.find_cart_by_customer_id(customer_id)
        return cart, 200 if cart else 404

    def post(self, customer_id):
        request_data = request.json()
        cart = model.add_item_to_cart(customer_id)
        return request_data, 200 if cart else 400

    def put(self, customer_id):
        request_data = request.json()
        item = model.edit_item_from_cart(customer_id, request)
        if item is None:
            return { "message": "Failed to edit item form cart" }, 400
        else:
            return request_data        
        
    def delete(self, customer_id):
        return { "message": "Item has been removed from cart" }