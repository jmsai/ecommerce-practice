from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def orders_response(data):
    return convert_to_json(data["orders"])

def order_response(data, order_id):
    for order in data["orders"]:
        if order["order_id"] == order_id:
            return convert_to_json(order)
    return convert_to_json(
        { "message": "No order found" }
    )