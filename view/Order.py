from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def orders_response(orders):
    return convert_to_json(orders)

def order_response(order):
    return convert_to_json(order)