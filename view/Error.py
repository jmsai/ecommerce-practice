from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json

def error_404_response(e):
    return convert_to_json(
        {
            "status": 404,
            "message": "Page not found",
            "err_message": e
        }
    )