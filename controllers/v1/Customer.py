from models.v1.Customer import Customer

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Customer()


class CustomerController_v1(Resource):
    def get(self, customer_id):
        customer = model.find_user_by_id(customer_id)
        if customer is None:
            return {"message": "No customer found"}, 404
        else:
            return customer, 200


class SignupController_v1(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_user_by_email(data.get('email'))
        if customer is None:
            new_customer = Customer(
                                    data.get('email'),
                                    data.get('password'),
                                    data.get('first_name'),
                                    data.get('middle_name'),
                                    data.get('last_name')
                                    ).__dict__
            model.create_customer(new_customer)
            return new_customer, 201
        else:
            return {"message": "User already exists"}, 400


class LoginController_v1(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_user_by_email(data.get('email'))

        if customer is None:
            return {"message": "User not found"}, 400

        input_password = data["password"]
        password = customer['password']

        valid_password = model.is_password_valid(input_password, password)

        if not valid_password:
            return {"message": "Password does not match"}, 400

        return data, 200
