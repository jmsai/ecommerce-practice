import uuid
import json


def filter_result(data_key, to_find, table):
    return filter(lambda data: data[data_key] == to_find, table)


def remove_data(data_key, to_find, table):
    return filter(lambda data: data[data_key] != to_find, table)


def generate_id():
    return str(uuid.uuid4().fields[-1])[:8]


def generate_tracking_number():
    return str(uuid.uuid4().fields[-1])[:12]


def get_json(data):
    response = json.dumps(data)
    return json.loads(response)


def get_money_value(number):
    return '{0:.2f}'.format(number)
