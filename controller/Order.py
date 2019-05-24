from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from model.Order import Order
import view.Order as view

model = Order()

def show_all_orders(customer_id):
    orders = model.find_orders_by_customer(customer_id)
    return view.orders_response(orders)

def show_order(customer_id, order_id):
    order = model.find_order_by_id(customer_id, order_id)
    return view.order_response(order)