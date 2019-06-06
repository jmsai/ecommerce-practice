from models.v1.Customer import Customer

from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))


class CustomerModel(Customer):
    pass
