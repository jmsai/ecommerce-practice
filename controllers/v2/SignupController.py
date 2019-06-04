from helpers.v2.JSONHelper import get_json
from models.v2.CustomerModel import CustomerModel

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Customer = CustomerModel()


class SignupController_v2(Resource):
    def post(self):
        data = request.get_json()
        customer = Customer.find_by_email(data['email'])
        if customer is None:
            new_customer = CustomerModel(
                                    data.get('email'),
                                    data.get('password'),
                                    data.get('first_name'),
                                    data.get('middle_name'),
                                    data.get('last_name')
                                    ).__dict__
            Customer.add(new_customer)
            return get_json(new_customer), 201
        else:
            return {"message": "User already exists"}, 400
