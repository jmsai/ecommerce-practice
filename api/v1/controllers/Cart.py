from api.v1.common import get_response
from api.v1.models.Cart import Cart
from api.v1.views.CartView import CartView
from error.model import NotFoundError
from error.model import UnprocessableEntityError
from error.model import ResourceAlreadyExistError
from error.view import ErrorView

from flask import request
from flask_restful import Resource

model = Cart()
view = CartView()
ErrorView = ErrorView()


class CartController(Resource):
    def get(self, customer_id):
        cart = model.find_by_customer(customer_id)

        if cart is None:
            error = NotFoundError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 404)

        display = view.display_cart(cart)
        return get_response(display, 200)

    def post(self, customer_id):
        cart = model.find_by_customer(customer_id)

        if cart is not None:
            error = ResourceAlreadyExistError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 409)

        new_cart = Cart(customer_id, []).__dict__
        model.add(new_cart)
        new_cart["sub_total"] = model.get_sub_total(new_cart)
        new_cart["number_of_items"] = model.count_all_items(new_cart)
        new_cart["tax_amount"] = 0
        new_cart["total"] = 0

        return get_response(new_cart, 201)

    def put(self, customer_id):
        data = request.get_json()
        cart = model.find_by_customer(customer_id)

        if cart is None:
            error = NotFoundError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 404)

        item = model.add_item(cart, data)

        if item is None:
            error = UnprocessableEntityError()
            display = ErrorView.display(error)
            return get_response(display, 422)

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)

        display = view.display_cart(cart)
        return get_response(display, 200)


class ItemController(Resource):
    def put(self, customer_id, item_id):
        data = request.get_json()

        cart = model.find_by_customer(customer_id)

        if cart is None:
            error = NotFoundError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 404)

        item = model.edit_item(cart, item_id, data)

        if item is None:
            display = ErrorView.display(UnprocessableEntityError())
            return get_response(display, 422)

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)

        display = view.display_cart(cart)
        return get_response(display, 200)

    def delete(self, customer_id, item_id):
        cart = model.find_by_customer(customer_id)

        if cart is None:
            error = NotFoundError("Cart")
            display = ErrorView.display(error)
            return get_response(display, 404)

        item = model.remove_item(cart, item_id)

        if item is None:
            error = UnprocessableEntityError()
            display = ErrorView.display(error),
            return get_response(display, 422)

        cart["sub_total"] = model.get_sub_total(cart)
        cart["number_of_items"] = model.count_all_items(cart)
        cart["tax_amount"] = model.get_tax_amount(cart)
        cart["total"] = model.get_total(cart)

        display = view.display_cart(cart)
        return get_response(display, 200)
