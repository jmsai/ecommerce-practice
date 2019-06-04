import json


def get_json(data):
    response = json.dumps(data)
    return json.loads(response)
