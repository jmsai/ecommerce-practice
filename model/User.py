import bcrypt
import json
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from helper.Helper import convert_to_json, generate_id

class User:
    def __init__(self, id, email, password, user_type):
        self.id = generate_id,
        self.email = email,
        self.password = password.encode()
        self.user_type = user_type

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt(8))

    def is_password_valid(self, input_password):
        hashed = self.hash_password(input_password)
        if bcrypt.checkpw(self.password, hashed):
            return True
        else:
            return False

    def display_json(self):
        user = {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "user_type": self.user_type
        }
        return convert_to_json(user)