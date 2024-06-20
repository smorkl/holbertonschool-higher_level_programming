#!/usr/bin/python3
"""
class students
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list)
            return {attrs: getattr(self, attrs) for attrs in attr
                    if hasattr(self, attrs)}
        
        return self.__dict__
