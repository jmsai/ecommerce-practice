from controllers.v1.Order import OrderListController_v1

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))


class OrderListController_v2(OrderListController_v1):
    pass
