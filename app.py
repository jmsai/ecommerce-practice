from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_page():
    return "This is an indexpage"

@app.route('/<user_id>')
def profile_page(user_id):
    return "This is a profile of customer with id: %s" % user_id

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