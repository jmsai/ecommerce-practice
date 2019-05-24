from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from model.Customer import Customer
import view.Customer as view

model = Customer()

def signup_customer(request_data):
    return view.signup_response(request_data)

def login_customer(request_data):
    return view.login_response(request_data)

def show_customer_profile(customer_id):
    customer = model.find_user_by_id(customer_id)
    return view.profile_response(customer)