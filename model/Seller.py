import json
import uuid
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_sku

class Seller:
    def __init__(self, name, seller_type, business_address, phone_number='', website='',  brand_logo=None):
        self.sku = generate_sku()
        self.brand_logo = brand_logo
        self.name = name
        self.seller_type = seller_type
        self.business_address = business_address
        self.phone_number = phone_number
        self.website = website

    def get_address(self, street, city, state, zip_code, country):
        return {
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": country
        }

    def display_json(self):
        seller = {
            "sku": self.sku,
            "name": self.name,
            "brand_logo": self.brand_logo,
            "seller_type": self.seller_type,
            "business_address": self.business_address,
            "phone_number": self.phone_number,
            "website": self.website
        }
        return convert_to_json(seller)