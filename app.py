from routes.v1 import api_v1
from routes.v2 import api_v2

from flask import Flask, Blueprint
from flask_restful import Api
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

app = Flask(__name__)
api = Api(app)

app.register_blueprint(api_v1, url_prefix='/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')


# Error Page Route
# @app.errorhandler(404)
# def page_not_found(e):
#     return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run(port=3000, debug=True)
