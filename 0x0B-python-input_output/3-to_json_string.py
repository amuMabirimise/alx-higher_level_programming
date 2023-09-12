#!/usr/bin/python3

import json  # Import the json module

def to_json_string(my_obj):
    """
    Convert an object to its JSON representation as a string.

    Args:
        my_obj: The Python object to be serialized to JSON.

    Returns:
        str: A JSON string representing the object.
    """
    # Use json.dumps to serialize the object to a JSON-formatted string
    json_string = json.dumps(my_obj)
    
    return json_string
