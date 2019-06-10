from controllers.v1.Customer import SignupController_v1

from os import path
import sys
from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))


class SignupController(SignupController_v1):
    pass
