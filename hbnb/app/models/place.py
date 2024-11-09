from datetime import datetime
from amenity import Amenity
from user import User
import uuid
from similitudes import Similitudes

class Place(Similitudes):
    def __init__(self, title, price, latitude, longitude, owner, description=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self._title = title
        self._description = description
        self._price = price
        self._latitude = latitude
        self._longitude = longitude
        self._owner = owner
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.reviews = [] #list of opinions from place 
        self.amenities = []

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
    def title(self):
        """
        returns the title of the place 
        """
        return self._title

    @title.setter
    def title(self, value, max_length=100):
        """
        validates the value of the title that meets certain specifications
        arg
            value(str) = Title of the place
            max_length(int) =  maximum length that the title must meet(50)
        raise
            ValueError: If the provided title exceeds the maximum length.
        """
        if len(value) > max_length:
            raise ValueError(f"The title cannot exceed the maximum length of {max_length} characters")
        self._title = value
    
    @property
    def price(self):
        """
        return the price of place 
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Validate the price of the place that meets certain specifications
        arg
            value(int) = price of the place
        raise
            ValueError = if the price of the place is negative
        """
        if value <= 0:
            raise ValueError("The price must be positive.")
        self._price = value
    
    @property
    def latitude(self):
        """
        return latitude of place
        """
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        """
        Validates the latitude of the location following some requirements
        arg
            value(float) = latitude of the place
        raise
            ValueError = if the latitude is not between 180.0 and -180.0
        """
        if not -90.0 <= value <= 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self._latitude = value

    @property
    def longitude(self):
        """
        return longitude of place
        """
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        """
        Validates the longitude of the location following some requirements
        arg
            value(float) = longitude of the place
        raise
            ValueError = if the longitude is not between 180.0 and -180.0
        """
        if not -180.0 <= value <= 180.0:
            raise ValueError("longitude must be between -180.0 and 90.0")
        self._longitude = value

    def add_amenity(self, amenity):
        """Add an amenity if it does not already exist in the list."""
        if not any(a.name == amenity.name for a in self.amenities):
            self.amenities.append(amenity)

    def remove_amenity(self, amenity_name):
        """Remove an amenity if it exists in the list, searching for it by name."""
        self.amenities = [a for a in self.amenities if a.name != amenity_name]

    def add_review(self, review):
        # Logic to associate the review with the Place object
        # This could involve adding the review to a list or storing it in a database
        self.reviews.append(review)# Placeholder for actual implementation
