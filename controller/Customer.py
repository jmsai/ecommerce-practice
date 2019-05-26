from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from flask import request
from flask_restful import Resource

from model.Customer import Customer
import view.Customer as view

model = Customer()

class CustomerController(Resource):
    def get(self, customer_id):
        customer = model.find_user_by_id(customer_id)
        return customer, 200 if customer else 404

class SignupController(Resource):
    def post(self):
        return request.get_json()

class LoginController(Resource):
    def post(self):
        return request.get_json()