from helpers.Helper import generate_id
from helpers.Helper import filter_result

import bcrypt
import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
customers = []


class Customer:
    def __init__(self, email='', password='', first_name='',
                 middle_name='', last_name='', phone_number='',
                 billing_address='', shipping_address=''):
        self.customer_id = generate_id()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.billing_address = billing_address
        self.shipping_address = shipping_address

    def hash(self, _password):
        return bcrypt.hashpw(_password.encode(), bcrypt.gensalt(8))

    def is_password_valid(self, _password, password):
        hashed = self.hash(_password)
        
        if bcrypt.checkpw(password.encode(), hashed):
            return True

        return False

    def find_all(self):
            return customers

    def find_by(self, _id):
        customers = self.find_all()
        customer = filter_result('customer_id', _id, customers)
        return next(customer, None)

    def find_by_email(self, _email):
        customers = self.find_all()
        customer = filter_result('email', _email, customers)
        return next(customer, None)

    def add(self, new_customer):
        customers.append(new_customer)

    def get_middle_initial(self, customer):
        return f'{customer["middle_name"][0]}.'

    def get_full_name(self, customer):
        first_name = customer["first_name"]
        middle_initial = customer["middle_initial"]
        last_name = customer["last_name"]
        return f'{first_name} {middle_initial} {last_name}'

    def get_address(self, street, city,
                    state, zip_code, country):
        return {
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": country
        }
