import bcrypt
import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_id

class Customer:
    def __init__(self, email, password, first_name, 
                 last_name, middle_name='', phone_number='', gender='', 
                 birth_date='', billing_address='', shipping_address=''):
        self.customer_id = generate_id(),
        self.email = email,
        self.password = password.encode()
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

    def is_password_valid(self, input_password):
        hashed = self.hash_password(input_password)
        if bcrypt.checkpw(self.password, hashed):
            return True
        else:
            return False

    def find_user_by_id(self, input_user_id):
        return input_user_id

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