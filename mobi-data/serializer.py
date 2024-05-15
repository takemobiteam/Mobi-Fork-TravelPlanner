import json
from definitions import Serializable
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super(CustomEncoder, self).__init__(*args, **kwargs)
        self.seen = {}
        self.counter = 1

    def default(self, obj):
        if isinstance(obj, datetime):
            return datetime_to_unix(obj)
        if isinstance(obj, Serializable):
            if id(obj) in self.seen:
                # If already serialized, return a reference ID
                return self.seen[id(obj)]
            # Assign a new ID and serialize for the first time
            obj_id = self.counter
            self.seen[id(obj)] = obj_id
            self.counter += 1
            # Merge '@id' with the JSON output of the object
            serialized_obj = {"@id": obj_id, **obj.to_json()}
            # Recursively serialize objects within the to_json result
            for key, value in serialized_obj.items():
                if isinstance(value, list):
                    serialized_obj[key] = [self.default(v) if isinstance(v, Serializable) else v for v in value]
                elif isinstance(value, Serializable):
                    serialized_obj[key] = self.default(value)
            return serialized_obj
        return super(CustomEncoder, self).default(obj)


def datetime_to_unix(date_object):
    if date_object is None:
        return None
    return int(date_object.timestamp())
