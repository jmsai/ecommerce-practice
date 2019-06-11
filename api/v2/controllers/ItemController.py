from api.v2.models.CartModel import CartModel
from api.v2.views.CartView import CartView
from api.v2.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

Cart = CartModel()
CartView = CartView()
Error = ErrorView()


class ItemController(Resource):
    def put(self, cart_id, customer_id, item_id):
        try:
            data = request.get_json()
            cart = Cart.find_by_customer(customer_id)
            item = Cart.edit_item(cart, item_id, data)

            if item is None:
                return Error.item_not_found(), 404

            cart["sub_total"] = model.get_sub_total(cart)
            cart["number_of_items"] = model.count_all_items(cart)
            cart["tax_amount"] = model.get_tax_amount(cart)
            cart["total"] = model.get_total(cart)

            return CartView.display_cart(cart), 200

        except:
            return Error.failed_to_perform_action(), 422

    def delete(self, cart_id, customer_id, item_id):
        try:
            cart = Cart.find_by_customer(customer_id)
            item = Cart.remove_item(cart, item_id)

            if item is None:
                return Error.item_not_found(), 404

            cart["sub_total"] = model.get_sub_total(cart)
            cart["number_of_items"] = model.count_all_items(cart)
            cart["tax_amount"] = model.get_tax_amount(cart)
            cart["total"] = model.get_total(cart)

            return CartView.display_cart(cart), 200

        except:
            return Error.failed_to_perform_action(), 422
