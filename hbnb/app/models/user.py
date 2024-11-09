from datetime import datetime
import re
import uuid
from similitudes import Similitudes

class User(Similitudes):
    def __init__(self, first_name, last_name, email, is_admin=False, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self.is_admin = is_admin
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.opinions = [] #list of opinions associated with the user


    @property
    def first_name(self):
        """Returns the user's first name.
        """
        return self._first_name
    
    @first_name.setter
    def first_name(self, value, max_length=50):
        """
        Sets the user's first name with validation for maximum length.

        Args:
            value (str): The new first name for the user.
            max_length (int, optional): The maximum allowed length for the first name (default 50).

        Raises:
            ValueError: If the provided first name exceeds the maximum length.
        """
        if len(value) > max_length:
            raise ValueError(f"The first name of the user. Required, maximum length of {max_length} characters")
        self._first_name = value

    @property
    def last_name(self):
        """Returns the user's last name.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value, max_length=50):
        """
        Sets the user's last name with validation for maximum length.

        Args:
            value (str): The last name for the user.
            max_length (int, optional): The maximum allowed length for the last name (default 50).

        Raises:
            ValueError: If the provided last name exceeds the maximum length.
        """
        if len(value) > max_length:
            raise ValueError(f"The last name cannot exceed the maximum length of {max_length} characters")
        self._last_name = value

    @property
    def email(self):
        """
        Returns the user's email address.
        """
        return self._email
    
    @email.setter
    def email(self, value):
        """
        Sets the user's email address with validation for format.

        Args:
            value (str): The new email address for the user.

        Raises:
            ValueError: If the provided email address does not conform to the expected format.
        """
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format")
        self._email = value

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")
    return user