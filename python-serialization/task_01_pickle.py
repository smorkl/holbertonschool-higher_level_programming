#!/usr/bin/python3
"""
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_students):
        self.name = name
        self.age = age
        self.is_students = is_students

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_students}")

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
