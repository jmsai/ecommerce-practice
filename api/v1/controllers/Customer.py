from api.v1.models.Customer import Customer
from api.v1.views.CustomerView import CustomerView
from api.v1.models.Error import NotFoundError
from api.v1.models.Error import BadRequestError
from api.v1.models.Error import UnprocessableEntityError
from api.v1.models.Error import ResourceAlreadyExistError
from api.v1.views.ErrorView import ErrorView

from flask import request
from flask_restful import Resource

model = Customer()
view = CustomerView()
ErrorView = ErrorView()


class CustomerController(Resource):
    def get(self, _id):
        try:
            customer = model.find_by(_id)
            customer["middle_initial"] = model.get_middle_initial(customer)
            customer["full_name"] = model.get_full_name(customer)

        except:
            error = NotFoundError("Customer")
            return ErrorView.display(error), 404

        else:
            return view.display(customer), 200


class SignupController(Resource):
    def post(self):
        try:
            data = request.get_json()
            customer = model.find_by_email(data["email"])

            if customer is not None:
                error = ResourceAlreadyExistError("User")
                return ErrorView.display(error), 409

        except:
            error = UnprocessableEntityError()
            return ErrorView.display(error), 422

        else:
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
        try:
            customer = model.find_by_email(data.get('email'))

            if customer is None:
                error = NotFoundError("Customer")
                return ErrorView.display(error), 404

        except:
            error = UnprocessableEntityError()
            return ErrorView.display(error), 422

        else:
            input_password = data["password"]
            password = customer['password']

            valid_password = model.is_password_valid(input_password, password)

            if not valid_password:
                error = BadRequestError("Login failed",
                                        "Password does not match")
                return ErrorView.display(error), 400

            return view.display_credentials(customer), 200
