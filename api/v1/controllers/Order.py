from api.v1.common import get_response
from api.v1.models.Order import Order
from api.v1.views.OrderView import OrderView
from error.model import NotFoundError
from error.model import BadRequestError
from error.model import UnprocessableEntityError
from error.model import ResourceAlreadyExistError
from error.view import ErrorView

from flask import request
from flask_restful import Resource

model = Order()
view = OrderView()
ErrorView = ErrorView()


class OrderController(Resource):
    def get(self, customer_id):
        orders = model.find_by_customer(customer_id)

        if orders is None:
            error = NotFoundError("Results")
            display = ErrorView.display(error)
            return get_response(display, 404)

        display = view.display_list(orders)
        return get_response(display, 200)

    def post(self, customer_id):
        data = request.get_json()

        new_order = Order(
                            data["customer_name"],
                            data["phone_number"],
                            data["shipping_address"],
                            data["billing_address"],
                            data["delivery_date"],
                            data["payment_method"],
                            data["payment_date"],
                            data["shipping_fee"],
                            data["tax_rate"],
                            data["items"],
                            customer_id
                        ).__dict__

        model.add(new_order)

        new_order["sub_total"] = model.get_sub_total(new_order)
        new_order["tax_amount"] = model.get_tax_amount(new_order)
        new_order["number_of_items"] = model.count_all_items(new_order)
        new_order["total"] = model.get_total(new_order)

        display = view.display_details(new_order)
        return get_response(display, 201)


class OrderDetailsController(Resource):
    def get(self, customer_id, order_id):
        order = model.find_by(order_id)

        if order is None:
            error = NotFoundError("Order Number")
            display = ErrorView.display(error)
            return get_response(display, 404)

        display = view.display_details(order)
        return get_response(display, 200)

    def put(self, customer_id, order_id):
        data = request.get_json()
        order = model.edit(customer_id, order_id, data)

        if order is None:
            error = NotFoundError("Order")
            display = ErrorView.display(error)
            return get_response(display, 404)

        return order, 200
