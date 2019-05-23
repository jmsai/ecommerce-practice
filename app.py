from flask import Flask, request
import json
app = Flask(__name__)


# User Routes
@app.route('/login')
def login_page():
    return "Login Page"

@app.route('/login', methods=['POST'])
def login_button():
    request_data = request.get_json()
    new_data = {
        "email": request_data["email"],
        "password": request_data["password"]
    }
    return json.dumps(new_data, indent=4)

@app.route('/signup')
def signup_page():
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



@app.route('/cart')
def cart_page():
    return "This is my Cart"

@app.route('/orders/<order_number>')
def order_page():
    return "This is an order page"

@app.route('/products/<product_sku>')
def product_page(product_sku):
    return "This is product ID: %s" % product_sku

@app.route('/sellers/<seller_sku>')
def seller_page(seller_sku):
    return "This is seller ID: %s" % seller_sku

@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()