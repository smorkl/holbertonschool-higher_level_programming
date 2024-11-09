from datetime import datetime
import uuid
from place import Place
from user import User
from similitudes import Similitudes

class Review(Similitudes):
    def __init__(self, comment, rating, place_id, user_id, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self._comment = comment
        self._rating = rating
        self._place_id = place_id
        self._user_id = user_id
        self.created_at =  created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    @property
    def rating(self):
        """return of rating the place
        """
        return self._rating
    
    @rating.setter
    def rating(self, value):
        """
        validate that the qualification meets the requirements
        arg
            value(int) = the rating given by the user of the place
        raise
            ValueError = If the value does not comply with the range between 1 to 5 
        """
        if not 1 <= value <= 5:
            raise ValueError("The rating must be between 1 and 5")
        self._rating = value

    @property
    def place(self):
        """Returns the owner of the place."""
        return self._place_id

    @place.setter
    def place(self, value):
        """Validates that the place is an instance of Place."""
        if not isinstance(value, Place):
            raise ValueError("Place must be a valid PLace instance.")
        self._place_id = value

    @property
    def owner(self):
        """Returns the owner of the place."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Validates that the owner is an instance of User."""
        if not isinstance(value, User):
            raise ValueError("Owner must be a valid User instance.")
        self._owner = value

    @property
    def comment(self):
        """return rewiew comment
        """
        return self._comment
    
    @comment.setter
    def comment(self, value):
        """
        """
        self._comment = value

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

def add_review(self, review):
    return self.review