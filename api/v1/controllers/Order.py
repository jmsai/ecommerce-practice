from api.v1.models.Order import Order
from api.v1.views.OrderView import OrderView
from api.v1.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

model = Order()
view = OrderView()
Error = ErrorView()


class OrderController(Resource):
    def get(self, customer_id):
        orders = model.find_by_customer(customer_id)

        if not orders:
            return Error.no_results_found(), 404

        return view.display_list(orders), 200

    def post(self, customer_id):
        try:
            data = request.get_json()

            new_order = Order(
                                data["customer_name"],
                                data["phone_number"],
                                data["shipping_address"],
                                data["billing_address"],
                                data["delivery_date"],
                                data["payment_date"],
                                data["payment_method"],
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

            return view.display_details(new_order), 201

        except:
            return Error.failed_to_perform_action(), 422


class OrderDetailsController(Resource):
    def get(self, customer_id, order_id):
        order = model.find_by(order_id)

        if order is None:
            return Error.order_number_not_found(), 404

        return view.display_details(order), 200

    def put(self, customer_id, order_id):
        try:
            data = request.get_json()
            order = model.edit(customer_id, order_id, data)

            if not order:
                return Error.no_results_found, 404

            return view.display_details(order), 200

        except:
            return Error.failed_to_perform_action(), 422
