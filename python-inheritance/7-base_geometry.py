#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry():
    """
    empty class BaseGeometry
    """
    def integer_validator(self, name, value):
        """
        The function validates if the value is
        an integer and if it is greater than 0
        raise
            TypeError and ValueError
        """
        if type(value) is not int:
            raise (TypeError("name must be an integer"))
        if value <= 0:
            raise (ValueError("name must be greater than 0"))

    def area(self):
        """
        this fuctio returns an exception error
        """
        raise (Exception("area() is not implemented"))
        pass
