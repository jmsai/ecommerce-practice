from api.v1.routes import api_v1
from api.v2.routes import api_v2
from api.v1.error import handle_page_not_found
from api.v1.error import handle_unauthorized_error
from api.v1.error import handle_access_denied_error
from api.v1.error import handle_internal_server_error

from flask import Flask, Blueprint
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.register_blueprint(api_v1, url_prefix='/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')

app.register_error_handler(404, handle_page_not_found)
app.register_error_handler(401, handle_unauthorized_error)
app.register_error_handler(403, handle_access_denied_error)
app.register_error_handler(500, handle_internal_server_error)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
