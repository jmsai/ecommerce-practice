from helpers.Helper import get_json
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
            orders = model.find_by_customer(customer_id)
            if not orders:
                return {"message": "No customer found"}, 404
            return get_json(orders), 200
        order = model.search_by(customer_id, order_id)
        if order is None:
            return {"message": "Order Number not found"}, 404
        return get_json(order), 200

    def post(self, customer_id):
        data = request.get_json()
        customer = model.find_by(customer_id)
        if customer is not None:
            return {"message": "Failed to add order"}, 400
        new_order = Order(
                            data.get('delivery_date'),
                            data.get('shipping_address'),
                            data.get('billing_address'),
                            data.get('payment_method'),
                            data.get('shipping_fee'),
                            data.get('items'),
                            customer_id
                        ).__dict__
        model.add(new_order)
        return get_json(new_order), 201


class OrderController_v1(Resource):
    def get(self, customer_id, order_id):
        order = model.find_by(order_id)
        if order is None:
            return {"message": "Order number not found"}, 404
        return get_json(order), 200

    def put(self, customer_id, order_id):
        data = request.get_json()
        order = model.edit(customer_id, order_id, data)
        if order is None:
            return {"message": "Failed to edit order"}, 400
        elif not order:
            return {"message": "Customer not found"}, 404
        else:
            return get_json(order), 200
