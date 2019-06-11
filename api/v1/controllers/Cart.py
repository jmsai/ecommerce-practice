from api.v1.models.Cart import Cart
from api.v1.views.CartView import CartView
from api.v1.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

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
        try:
            new_cart = Cart(customer_id, []).__dict__
            cart = model.find_by_customer(customer_id)

            if cart is not None:
                return Error.cart_already_exist(), 400

            model.add(new_cart)
            new_cart["sub_total"] = model.get_sub_total(new_cart)
            new_cart["number_of_items"] = model.count_all_items(new_cart)
            new_cart["tax_amount"] = 0
            new_cart["total"] = 0

            return new_cart, 201

        except:
            return Error.failed_to_perform_action(), 422

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
