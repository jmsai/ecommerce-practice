from api.v1.common import get_response
from api.v2.models.CartModel import CartModel
from api.v2.views.CartView import CartView
from api.v1.controllers.Cart import CartController as CartController_v1
from error.model import NotFoundError
from error.model import BadRequestError
from error.model import UnprocessableEntityError
from error.model import ResourceAlreadyExistError
from error.view import ErrorView

from flask import request
from flask_restful import Resource

Cart = CartModel()
CartView = CartView()
ErrorView = ErrorView()


class CartController(CartController_v1):
    def post(self, customer_id):
        cart = Cart.find_by_customer(customer_id)

        if cart is not None:
            error = ResourceAlreadyExistError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 409)

        new_cart = CartModel(customer_id, []).__dict__

        Cart.add(new_cart)

        new_cart["sub_total"] = Cart.get_sub_total(new_cart)
        new_cart["number_of_items"] = Cart.count_all_items(new_cart)
        new_cart["tax_amount"] = 0
        new_cart["total"] = 0

        return get_response(new_cart, 201)
