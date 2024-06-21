#!/usr/bin/python3
"""
This script defines a CustomObject class
that allows serialization and deserialization
of class instances to and from files using the
pickle module, with exception handling.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_students):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_students (bool): The student status of the object.
        """
        self.name = name
        self.age = age
        self.is_students = is_students

    def display(self):
        """
        Displays the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_students}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The name of the file to save the instance to.

        Returns:
            None: Returns None if an error occurs during serialization.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (EOFError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of the class from a file.

        Args:
            filename (str): The name of the file from
            which to load the instance.

        Returns:
            CustomObject: An instance of the class
            deserialized from the file, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (EOFError, pickle.PickleError) as e:
            print(f"Error deserializing object: {e}")
            return None
