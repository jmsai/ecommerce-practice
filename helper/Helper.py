import json
import uuid

def convert_to_json(obj):
    return json.dumps(obj, indent=4, sort_keys=False)

def generate_id():
    return str(uuid.uuid4().fields[-1])[:8]

def generate_tracking_number():
    return str(uuid.uuid4().fields[-1])[:12]