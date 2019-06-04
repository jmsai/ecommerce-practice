def filter_result(data_key, to_find, table):
    return filter(lambda data: data[data_key] == to_find, table)


def remove_data(data_key, to_find, table):
    return filter(lambda data: data[data_key] != to_find, table)
