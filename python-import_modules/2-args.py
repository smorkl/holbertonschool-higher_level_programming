#!/usr/bin/python3

import sys

def print_args(args):
  """Prints information about the arguments passed to the script.

  Args:
    args: A list of strings representing the command-line arguments.
  """

  num_args = len(args) - 1
  if num_args == 0:
    print("0 arguments.")
  elif num_args == 1:
    print(f"1 argument:\n1: {args[1]}")
  else:
    print(f"{num_args} arguments:")
    for i in range(1, len(args)):
      print(f"{i}: {args[i]}")

if __name__ == "__main__":
  print_args(sys.argv)