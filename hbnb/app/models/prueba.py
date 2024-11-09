

class Place:
    def __init__(self, id, title, latitude, longitude, owner, amenities=None):
        self.id = id
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities = amenities if amenities is not None else []  # Lista de instancias Amenity

    def add_amenity(self, amenity):
        """Añade un amenity si no existe ya en la lista."""
        if not any(a.name == amenity.name for a in self.amenities):
            self.amenities.append(amenity)

    def remove_amenity(self, amenity_name):
        """Remueve un amenity si existe en la lista, buscándolo por nombre."""
        self.amenities = [a for a in self.amenities if a.name != amenity_name]

# Crear amenidades
wifi = Amenity(name="WiFi")
piscina = Amenity(name="Piscina")

# Crear un lugar y añadir amenities
place = Place(id="place_123", title="Apartamento", latitude=40.7128, longitude=-74.0060, owner="Juan")
place.add_amenity(wifi)
place.add_amenity(piscina)


# Imprimir nombres de amenities
print([amenity.name for amenity in place.amenities])  # ['WiFi', 'Piscina']

# Remover amenity
place.remove_amenity("WiFi")
print([amenity.name for amenity in place.amenities])  # ['Piscina']





"""
from datetime import datetime

class Place:
    def __init__(self, id, title, description, price, latitude, longitude, owner, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def set_title_with_max_length(self, title, max_length=5):  # Include 'self' as the first argument
        if len(title) > max_length:
            raise ValueError(f"The title cannot exceed the maximum length of {max_length} characters")
        self.title = title  # Update the title attribute within the method using 'self'
        return title

place = Place("place_123", "A very long title", "description", 100.0, 48.8566, 2.3522, "pedro")
# Call the method explicitly providing the title and using 'self' implicitly
place.set_title_with_max_length("A very long title")
print(place.title)  # This will now print the first 5 characters (or raise an error if exceeding 5)
"""