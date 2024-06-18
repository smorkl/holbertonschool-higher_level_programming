#!/usr/bin/python3
"""
save_to_json_filet
"""
import json

def save_to_json_file(my_obj, filename):
  """Saves an object to a text file using its JSON representation.

  Args:
      my_obj: The Python object to save.
      filename: The name of the file to write to.
  """

  with open(filename, "w", encoding="utf-8") as f:
    json.dump(my_obj, f)
