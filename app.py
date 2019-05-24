from flask import Flask, request
import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

import controller.Product as ProductController
import controller.Customer as CustomerController
import controller.Cart as CartController
import controller.Order as OrderController

app = Flask(__name__)

# User Routes
@app.route('/login', methods=['POST', 'GET'])
def login_button():
    if request.method == 'POST':
        request_data = request.get_json()
        return CustomerController.login_customer(request_data)
    else:
        return "Login Page"

@app.route('/signup', methods=['POST', 'GET'])
def signup_button():
    if request.method == 'POST':
        request_data = request.get_json()
        return CustomerController.signup_customer(request_data)
    else:
        return "Signup Page"

@app.route('/customers/<customer_id>')
def profile_page(customer_id):
    return CustomerController.show_customer_profile(customer_id)

# Product Routes
@app.route('/')
def index_page():
    return ProductController.show_all_products()

@app.route('/products/<product_id>')
def product_page(product_id):
    return ProductController.show_product_details(product_id)

# Cart Routes
@app.route('/cart/<customer_id>')
def cart_page(customer_id):
    with open('seed.json', 'r') as seed_file:
        data = json.load(seed_file)
        for cart in data["carts"]:
            if cart["customer_id"] == customer_id:
                return json.dumps(cart, indent=4)
    return json.dumps({"message": "User does not exist"}, indent=4)



# @app.route('/cart/item/<int:id>', methods=['DELETE'])
# def delete_item_from_cart_button(id):
#     pass


# Order Routes
@app.route('/orders')
def orders_page():
    with open('seed.json', 'r') as seed_file:
        data = json.load(seed_file)
    return json.dumps(data["orders"], indent=4)

@app.route('/order/<order_number>')
def order_page(order_number):
    with open('seed.json', "r") as seed_file:
        data = json.load(seed_file)
        for order in data["orders"]:
            if order["order_number"] == order_number:
                return json.dumps(order, indent=4)
    return json.dumps({"message": "No order found"}, indent=4)


# Error Page Route
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()

app.run(port=3000)