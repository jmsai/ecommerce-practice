from helpers.JSONHelper import get_json
from models.CustomerModel import CustomerModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Customer = CustomerModel()


class CustomerController(Resource):
    def get(self, _id):
        customer = Customer.find_by(_id)
        if customer is None:
            return {"message": "No customer found"}, 404
        return get_json(customer), 200
