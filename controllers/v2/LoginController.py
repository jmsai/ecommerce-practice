from helpers.v2.JSONHelper import get_json 
from models.v2.CustomerModel import CustomerModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Customer = CustomerModel()


class LoginController_v2(Resource):
    def post(self):
        data = request.get_json()
        customer = Customer.find_by_email(data['email'])

        if customer is None:
            return {"message": "User not found"}, 400

        _password = data["password"]
        password = customer['password']

        valid_password = Customer.is_password_valid(_password, password)

        if not valid_password:
            return {"message": "Password does not match"}, 400

        return get_json(customer), 200
