from helpers.Helper import get_json
from models.v1.Customer import Customer

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Customer()


class CustomerController_v1(Resource):
    def get(self, _id):
        customer = model.find_by(_id)
        if customer is None:
            return {"message": "No customer found"}, 404
        return get_json(customer), 200


class SignupController_v1(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_by_email(data.get('email'))
        if customer is not None:
            return {"message": "User already exists"}, 400
        new_customer = Customer(
                                data.get('email'),
                                data.get('password'),
                                data.get('first_name'),
                                data.get('middle_name'),
                                data.get('last_name')
                                ).__dict__
        model.add(new_customer)
        return get_json(new_customer), 201


class LoginController_v1(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_by_email(data.get('email'))

        if customer is None:
            return {"message": "User not found"}, 400

        input_password = data["password"]
        password = customer['password']

        valid_password = model.is_password_valid(input_password, password)

        if not valid_password:
            return {"message": "Password does not match"}, 400

        return get_json(data), 200
