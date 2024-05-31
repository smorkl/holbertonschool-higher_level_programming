#!/usr/bin/python3

class Square:
    """
    This class represents a square shape.

    Currently, it only defines a constructor that prints a simple string
    representation of a square using curly braces `{}`. However, you can extend
    this class to add functionalities specific to squares, such as calculating
    area, perimeter, or drawing a more visually appealing representation.

    **Docstring checks:**

    - To view the docstring of this class:
        ```bash
        python3 -c 'print(__import__("your_module_name").Square.__doc__)'
        ```
        Replace `your_module_name` with the actual name of the file
        containing this class.
    """

    def __init__(self):
        """
        The constructor of the Square class.

        When creating a Square object, this method is automatically called
        and prints the string representation of the square (`{}`).

        **Docstring checks:**

        - There is currently no docstring available for the constructor.
        ```bash
        # This will not print anything as there's no __doc__ for __init__
        python3 -c 'print(__import__("your_module_name")
        .Square.__init__.__doc__)'
        ```
        Replace `your_module_name` with the actual module name.
        """

        a = '{'
        b = '}'
        print("{}{}".format(a, b))  # Print the square representation
