from models.v1.Customer import Customer
from views.v1.CustomerView import CustomerView
from views.v1.ErrorView import ErrorView

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
model = Customer()
view = CustomerView()
Error = ErrorView()


class CustomerController(Resource):
    def get(self, _id):
        customer = model.find_by(_id)

        if customer is None:
            return Error.customer_not_found(), 404

        customer["middle_initial"] = model.get_middle_initial(customer)
        customer["full_name"] = model.get_full_name(customer)

        return view.display(customer), 200


class SignupController(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_by_email(data["email"])

        if customer is not None:
            return Error.user_already_exist(), 400

        new_customer = Customer(
                                data["email"],
                                data["password"],
                                data["first_name"],
                                data["middle_name"],
                                data["last_name"]
                                ).__dict__

        model.add(new_customer)

        return view.display_credentials(new_customer), 201


class LoginController(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_by_email(data.get('email'))

        if customer is None:
            return Error.user_not_found(), 404

        input_password = data["password"]
        password = customer['password']

        valid_password = model.is_password_valid(input_password, password)

        if not valid_password:
            return Error.invalid_login(), 400

        return view.display_credentials(customer), 200
