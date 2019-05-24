from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def login_response(request_data):
    return convert_to_json(
        {
            "email": request_data["email"],
            "password": request_data["password"]
        }
    )

def signup_response(request_data):
    return convert_to_json(
        {
            "email": request_data["email"],
            "password": request_data["password"],
            "name": {
                "first_name": request_data["first_name"],
                "middle_name": request_data["middle_name"],
                "last_name": request_data["last_name"]
            }
        }
    )

def profile_response(customer):
    return convert_to_json(customer)