import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_id

class Customer:
    def __init__(self, first_name, last_name, phone_number = '', gender = '', birth_date = '', billing_address = '', shipping_address = ''):
        self.id = generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender
        self.birth_date = birth_date
        self.billing_address = billing_address
        self.shipping_address = shipping_address

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
    
    def display_json(self):
        customer = {
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name": self.last_name,
            "phone_number" : self.phone_number,
            "gender" : self.gender,
            "birth_date" : self.birth_date,
            "billing_address": self.billing_address,
            "shipping_address" : self.shipping_address         
        }
        return convert_to_json(customer)