from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from model.Product import Product
import view.Product as view

model = Product()

def show_all_products():
    products = model.find_all_products()
    return view.index_response(products)

def show_product_details(product_id):
    product = model.find_product_by_id(product_id)
    return view.product_response(product)