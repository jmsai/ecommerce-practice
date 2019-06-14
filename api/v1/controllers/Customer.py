from api.v1.common import get_response
from api.v1.models.Customer import Customer
from api.v1.views.CustomerView import CustomerView
from error.model import NotFoundError
from error.model import BadRequestError
from error.model import UnprocessableEntityError
from error.model import ResourceAlreadyExistError
from error.view import ErrorView

from flask import request
from flask_restful import Resource

model = Customer()
view = CustomerView()
ErrorView = ErrorView()


class CustomerController(Resource):
    def get(self, _id):
            customer = model.find_by(_id)

            if customer is None:
                display = ErrorView.display(NotFoundError("Customer"))
                return get_response(display, 404)

            customer["middle_initial"] = model.get_middle_initial(customer)
            customer["full_name"] = model.get_full_name(customer)

            display = view.display(customer)
            return get_response(display, 200)


class SignupController(Resource):
    def post(self):
        data = request.get_json()

        customer = model.find_by_email(data["email"])

        if customer is not None:
            error = ResourceAlreadyExistError("User")
            display = ErrorView.display(error)
            return get_response(display, 409)

        new_customer = Customer(
                                data["email"],
                                data["password"],
                                data["first_name"],
                                data["middle_name"],
                                data["last_name"]
                                ).__dict__

        model.add(new_customer)
        display = view.display_credentials(new_customer)

        return get_response(display, 201)


class LoginController(Resource):
    def post(self):
        data = request.get_json()
        customer = model.find_by_email(data.get('email'))

        if customer is None:
            error = NotFoundError("Customer")
            display = ErrorView.display(error)
            return get_response(display, 404)

        input_password = data["password"]
        password = customer['password']

        valid_password = model.is_password_valid(input_password, password)

        if not valid_password:
            error = BadRequestError("Login failed",
                                    "Password does not match")
            display = ErrorView.display(error)
            return get_response(display, 400)

        display = view.display_credentials(customer)
        return get_response(display, 200)
