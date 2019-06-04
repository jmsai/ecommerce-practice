import uuid


def filter_result(data_key, to_find, table):
    return filter(lambda data: data[data_key] == to_find, table)


def remove_data(data_key, to_find, table):
    return filter(lambda data: data[data_key] != to_find, table)


def generate_id():
    return str(uuid.uuid4().fields[-1])[:8]


def generate_tracking_number():
    return str(uuid.uuid4().fields[-1])[:12]
