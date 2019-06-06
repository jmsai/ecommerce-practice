from controllers.v1.Order import OrderController_v1

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))


class OrderController_v2(OrderController_v1):
    pass
