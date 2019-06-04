import routes.v1 as Routes_v1
import routes.v2 as Routes_v2

from flask import Flask
from flask_restful import Api
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

app = Flask(__name__)
api = Api(app)

Routes_v1.routes(api)
Routes_v2.routes(api)


# Error Page Route
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: Page not found!"

if __name__ == '__main__':
    app.run()

app.run(port=3000)
