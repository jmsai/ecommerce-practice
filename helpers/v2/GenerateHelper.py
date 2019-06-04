import uuid


def generate_id():
    return str(uuid.uuid4().fields[-1])[:8]


def generate_tracking_number():
    return str(uuid.uuid4().fields[-1])[:12]
