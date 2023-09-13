def to_json_string(my_obj):
  """Returns the JSON representation of an object (string).

  Args:
    my_obj: The object to serialize.

  Returns:
    The JSON representation of the object.
  """

  import json

  return json.dumps(my_obj)
