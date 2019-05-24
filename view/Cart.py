from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def cart_response(cart):
    convert_to_json(cart)