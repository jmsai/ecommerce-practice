from helpers.JSONHelper import get_json
from models.OrderModel import OrderModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Order = OrderModel()


class OrderListController(Resource):
    def get(self, customer_id):
        order_id = request.args.get('order_id')
        if order_id is None:
            orders = Order.find_by_customer(customer_id)
            if not orders:
                return {"message": "No customer found"}, 404
            return get_json(orders), 200
        order = Order.search_by(customer_id, order_id)
        if order is None:
            return {"message": "Order Number not found"}, 404
        return get_json(order), 200

    def post(self, customer_id):
        data = request.get_json()
        customer = Order.find_by_customer(customer_id)
        if customer is None:
            new_order = OrderModel(
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
            Order.add(new_order)
            return get_json(new_order), 201
        return {"message": "Failed to add order"}, 400
