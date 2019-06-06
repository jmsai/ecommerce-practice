from controllers.v1.Customer import CustomerController_v1

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))


class CustomerController_v2(CustomerController_v1):
    pass
