from helpers.v1.Helper import filter_result, generate_id

import bcrypt
import json
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))
customers = []


class Customer:
    def __init__(self, email='', password='', first_name='',
                 last_name='', middle_name='', phone_number='', gender='',
                 birth_date='', billing_address='', shipping_address=''):
        self.customer_id = generate_id()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender
        self.birth_date = birth_date
        self.billing_address = billing_address
        self.shipping_address = shipping_address

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt(8))

    def is_password_valid(self, input_password, password):
        hashed = self.hash_password(input_password)
        if bcrypt.checkpw(password.encode(), hashed):
            return True
        else:
            return False

    def find_all_users(self):
            return customers

    def find_user_by_id(self, customer_id):
        customers = self.find_all_users()
        customer = filter_result('customer_id', customer_id, customers)
        return next(customer, None)

    def find_user_by_email(self, customer_email):
        customers = self.find_all_users()
        customer = filter_result('email', customer_email, customers)
        return next(customer, None)

    def create_customer(self, new_customer):
        customers.append(new_customer)

    def get_full_name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    def get_address(self, street, city, state, zip_code, country):
        return {
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": country
        }
