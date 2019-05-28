from model.Order import Order

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Order()


class OrderListController(Resource):
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
        request_data = request.json()
        customer = model.add_order(customer_id, request_data)
        if customer is None:
            return {"message": "Failed to add order"}, 400
        else:
            return request_data, 201


class OrderController(Resource):
    def get(self, order_id):
        order = model.find_order_by_id(order_id)
        if order is None:
            return {"message": "Order number not found"}, 404
        else:
            return order, 200

    def put(self, order_id):
        request_data = request.json()
        order = model.edit_order(order_id, request_data)
        if order is None:
            return {"message": "Failed to edit order"}, 400
        else:
            return request_data

    def delete(self, order_id):
        return {"message": "Order has been cancelled"}
