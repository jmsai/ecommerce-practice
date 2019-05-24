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
@app.route('/orders/<customer_id>')
def orders_page(customer_id):
    return OrderController.show_all_orders(customer_id)

@app.route('/orders/<customer_id>', methods=['POST'])
def checkout_cart_button(cart):
    pass

@app.route('/orders/<customer_id>', methods=['PUT'])
def confirm_payment_button(cart_id):
    pass

@app.route('/order/<customer_id>')
def order_page(customer_id):
    order_id = request.args.get('id')
    return OrderController.show_order(customer_id, order_id)

@app.route('/order/<customer_id>?order_id=<order_number>', methods=['PUT'])
def change_shipment_status(order_number):
    pass

@app.route('/order/<customer_id>?order_id=<order_number>', methods=['DELETE'])
def cancel_shipment(order_number):
    pass


# Error Page Route
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()

app.run(port=3000)