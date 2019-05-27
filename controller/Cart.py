from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask import request
from flask_restful import Resource

from model.Cart import Cart

model = Cart() 

class CartController(Resource):
    def get(self, customer_id):
        cart = model.find_cart_by_customer_id(customer_id)
        if cart is None:
            return { "message": "Customer not found" }, 404
        else:
            return cart, 200

    def post(self, customer_id):
        request_data = request.get_json()
        cart = model.add_item_to_cart(customer_id, request_data)
        if cart is None:
            return { "message": "Failed to add item to cart" }, 400
        else:
            return cart, 201

    def put(self, customer_id):
        request_data = request.get_json()
        item = model.edit_item_from_cart(customer_id, request_data) 
        if item is None:
            return { "message": "Failed to edit item from cart" }, 400
        else:
            return item, 200
        
    def delete(self, customer_id):
        return { "message": "Item has been removed from cart" }