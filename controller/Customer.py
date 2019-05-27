from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask import request
from flask_restful import Resource 

from model.Customer import Customer

model = Customer()

class CustomerController(Resource):
    def get(self, customer_id):
        customer = model.find_user_by_id(customer_id)
        if customer is None:
            return { "message": "No customer found" }, 404
        else:           
            return customer, 200

class SignupController(Resource):
    def post(self):
        return request.get_json()

class LoginController(Resource):
    def post(self):
        return request.get_json()