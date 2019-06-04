from models.v1.Order import Order

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Order()


class OrderListController_v1(Resource):
    def get(self, customer_id):
        order_id = request.args.get('order_id')

        if order_id is None:
            orders = model.find_orders_by_customer(customer_id)

            if not orders:
                return {"message": "No customer found"}, 404
            else:
                return orders, 200

        else:
            order = model.search_order_by_id(customer_id, order_id)

            if order is None:
                return {"message": "Order Number not found"}, 404
            else:
                return order, 200

    def post(self, customer_id):
        data = request.get_json()
        customer = model.find_order_by_id(customer_id)

        if customer is None:
            new_order = Order(
                                data.get('delivery_date'),
                                data.get('shipping_address'),
                                data.get('billing_address'),
                                data.get('payment_method'),
                                data.get('tax_amount'),
                                data.get('shipping_fee'),
                                data.get('discount_total'),
                                data.get('payment_total'),
                                data.get('items'),
                                customer_id
                            ).__dict__
            model.add_order(new_order)
            return new_order, 201
        else:
            return {"message": "Failed to add order"}, 400


class OrderController_v1(Resource):
    def get(self, customer_id, order_id):
        order = model.find_order_by_id(order_id)

        if order is None:
            return {"message": "Order number not found"}, 404
        else:
            return order, 200

    def put(self, customer_id, order_id):
        data = request.get_json()
        order = model.edit_order(customer_id, order_id, data)

        if order is None:
            return {"message": "Failed to edit order"}, 400
        elif not order:
            return {"message": "Customer not found"}, 404
        else:
            return order, 200
