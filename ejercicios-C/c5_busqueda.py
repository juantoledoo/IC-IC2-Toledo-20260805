peliculas = [
    {"titulo": "the shutter island", "anio": 2010, "director": "Martin Scorsese"},
    {"titulo": "spiderman no way home", "anio": 2021, "director": "Jon Watts"},
    {"titulo": "Interestellar", "anio": 2014, "director": "Christopher Nolan"}
]

busqueda = "Scorsese"
encontradas = []

for pelicula in peliculas:
    if busqueda in pelicula["director"]:
        encontradas.append(pelicula["titulo"])

if len(encontradas) > 0:
    print("Peliculas encontradas:", encontradas)
else:
    print("No se encontraron peliculas de ese director")