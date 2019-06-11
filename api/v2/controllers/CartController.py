from api.v2.models.CartModel import CartModel
from api.v1.controllers.Cart import CartController as CartController_v1
from api.v2.views.CartView import CartView
from api.v2.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

Cart = CartModel()
CartView = CartView()
Error = ErrorView()


class CartController(CartController_v1):
    def post(self, customer_id):
        try:
            new_cart = CartModel(customer_id, []).__dict__
            cart = Cart.find_by_customer(customer_id)

            if cart is not None:
                return Error.cart_already_exist(), 400

            Cart.add(new_cart)
            new_cart["sub_total"] = Cart.get_sub_total(new_cart)
            new_cart["number_of_items"] = Cart.count_all_items(new_cart)
            new_cart["tax_amount"] = 0
            new_cart["total"] = 0

            return new_cart, 201

        except:
            return Error.failed_to_perform_action(), 422
