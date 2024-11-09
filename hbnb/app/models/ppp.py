# Crear amenidades
wifi = Amenity(id=1, name="WiFi")
piscina = Amenity(id=2, name="Piscina")



# Crear un lugar y añadir amenities
place = Place(id="place_123", title="Apartamento", latitude=40.7128, longitude=-74.0060, owner="Juan", price=5000)
place.add_amenity(wifi)
place.add_amenity(piscina)


# Imprimir nombres de amenities
print([amenity.name for amenity in place.amenities])  # ['WiFi', 'Piscina']

# Remover amenity

print([amenity.name for amenity in place.amenities])  # ['Piscina']
print(wifi.created_at)
wifi.name = "wifi premium"
wifi.save()


print(wifi.updated_at)
print([amenity.name for amenity in place.amenities])  # ['WiFi', 'Piscina']




try:
    place = Place(id="place_123", title="Beautiful Spot", description="A wonderful place to visit", 
                  price=100, latitude=45.0, longitude=-75.0, owner="Pedro")
    print(f"Place created: {place.title}, Price: {place.price}, Latitude: {place.latitude}, Longitude: {place.longitude}")
except ValueError as e:
    print("Error al crear la instancia con valores válidos:", e)

# Prueba con un título que excede la longitud máxima
try:
    place.title = "A" * 101  # Título de 101 caracteres, el máximo es 100
except ValueError as e:
    print("Error de título:", e)

# Prueba con un precio negativo
try:
    place.price = -10
except ValueError as e:
    print("Error de precio:", e)

# Prueba con una latitud fuera del rango permitido
try:
    place.latitude = 91.0  # Latitud fuera del rango permitido de -90.0 a 90.0
except ValueError as e:
    print("Error de latitud:", e)

# Prueba con una longitud fuera del rango permitido
try:
    place.longitude = 181.0  # Longitud fuera del rango permitido de -180.0 a 180.0
except ValueError as e:
    print("Error de longitud:", e)