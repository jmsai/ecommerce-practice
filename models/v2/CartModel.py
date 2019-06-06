from helpers.Helper import generate_id
from helpers.Helper import filter_result
from models.v1.Cart import Cart

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class CartModel(Cart):
    def __init__(self, customer_id='', items=''):
        super().__init__(customer_id, items)
        self._id = generate_id()
