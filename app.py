from flask import Flask, request
import json
app = Flask(__name__)


# User Routes
@app.route('/login', methods=['POST', 'GET'])
def login_button():
    if request.method == 'POST':
        request_data = request.get_json()
        new_data = {
            "email": request_data["email"],
            "password": request_data["password"]
        }
        return json.dumps(new_data, indent=4)
    else:
        return "Login Page"

@app.route('/signup', methods=['POST', 'GET'])
def signup_button():
    if request.method == 'POST':
        request_data = request.get_json()
        new_data = {
            "email": request_data["email"],
            "password": request_data["password"],
            "name": {
                "first_name": request_data["first_name"],
                "middle_name": request_data["middle_name"],
                "last_name": request_data["last_name"]
            }
        }
        return json.dumps(new_data, indent=4)
    else:
        return "Signup Page"

@app.route('/user/<id>')
def profile_page(id):
    with open('seed.json', 'r') as seed_file:
        data = json.load(seed_file)
        for user in data["users"]:
            if user["id"] == id:
                return json.dumps(user, indent=4)
    return json.dumps({"message": "No user exist"})

@app.route('/')
def index_page():
    with open('seed.json', "r") as seed_file:
        data = json.load(seed_file)
    return json.dumps(data['products'], indent=4)

#Product Route
@app.route('/product/<sku>')
def product_page(sku):
    with open('seed.json', 'r') as seed_file:
        data = json.load(seed_file)
        for product in data["products"]:
            if product["sku"] == sku:
                return json.dumps(product, indent=4)
    return json.dumps({"message": "No product found"}, indent=4)


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