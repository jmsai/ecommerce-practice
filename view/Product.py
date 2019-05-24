from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def index_response(products):
    return convert_to_json(products)

def product_response(product):
    return convert_to_json(product)