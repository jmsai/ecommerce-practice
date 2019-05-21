from helper.Helper import convert_to_json, generate_sku
from os import path
import sys

def get_dir_path():
    sys.path.append(path.join(path.dirname(__file__), '..'))
