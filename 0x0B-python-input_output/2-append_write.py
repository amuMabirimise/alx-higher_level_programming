#!/usr/bin/python3
"""defines a function"""


def append_write(filename="", text=""):
  """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

  Args:
    filename: The name of the file to append to.
    text: The string to append to the file.

  Returns:
    The number of characters added to the file.
  """

  with open(filename, "a", encoding="utf-8") as f:
    return f.write(text)
