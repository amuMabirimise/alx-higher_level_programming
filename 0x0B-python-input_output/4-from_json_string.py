#!/usr/bin/python3

def from_json_string(my_str):
  """Returns an object (Python data structure) represented by a JSON string.

  Args:
    my_str: The JSON string.

  Returns:
    The object represented by the JSON string.
  """

  import json

  try:
    return json.loads(my_str)
  except json.JSONDecodeError:
    return None
