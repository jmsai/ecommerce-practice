from models.v1.Order import Order

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class OrderModel(Order):
    pass
