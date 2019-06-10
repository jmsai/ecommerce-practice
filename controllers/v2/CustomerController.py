from controllers.v1.Customer import CustomerController

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))


class CustomerDetailsController(CustomerController):
    pass
