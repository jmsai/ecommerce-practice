from helpers.v2.JSONHelper import get_json
from models.v2.OrderModel import OrderModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Order = OrderModel()


class OrderController_v2(Resource):
    def get(self, order_id):
        order = Order.find_by(order_id)
        if order is None:
            return {"message": "Order number not found"}, 404
        return get_json(order), 200

    def put(self, customer_id, order_id):
        data = request.get_json()
        order = Order.edit(customer_id, order_id, data)
        if order is None:
            return {"message": "Failed to edit order"}, 400
        if not order:
            return {"message": "Customer not found"}, 404
        return get_json(order), 200
