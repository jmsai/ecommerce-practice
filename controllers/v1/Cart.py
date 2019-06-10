from models.v1.Cart import Cart
from views.v1.CartView import CartView
from views.v1.ErrorView import ErrorView

from os import path
import sys
import json

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Cart()
view = CartView()
Error = ErrorView()


class CartController(Resource):
    def get(self, customer_id):
        cart = model.find_by_customer(customer_id)

        if cart is None:
            return Error.customer_not_found(), 404

        return view.display_cart(cart), 200

    def post(self, customer_id):
        new_cart = Cart(customer_id, []).__dict__
        cart = model.find_by_customer(customer_id)

        if cart is None:
            model.add(new_cart)
            new_cart["sub_total"] = model.get_sub_total(new_cart)
            new_cart["number_of_items"] = model.count_all_items(new_cart)
            return new_cart, 201

        return Error.cart_already_exist(), 400

    def put(self, customer_id):
        data = request.get_json()
        cart = model.find_by_customer(customer_id)
        item = model.add_item(cart, data)

        if item is None:
            return Error.failed_to_perform_action(), 422

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)

        return view.display_cart(cart), 200


class ItemController(Resource):
    def put(self, customer_id, item_id):
        data = request.get_json()
        cart = model.find_by_customer(customer_id)
        item = model.edit_item(cart, item_id, data)

        if item is None:
            return Error.failed_to_perform_action(), 422

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)

        return view.display_cart(cart), 200

    def delete(self, customer_id, item_id):
        cart = model.find_by_customer(customer_id)
        item = model.remove_item(cart, item_id)

        if item is None:
            return Error.failed_to_perform_action(), 422

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)
        
        return view.display_cart(cart), 200
