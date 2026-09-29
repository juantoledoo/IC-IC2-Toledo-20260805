import csv
from pathlib import Path

ruta = Path(__file__).parent / "peliculas.csv"

peliculas = []

with open(ruta, encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        peliculas.append(fila)

cantidad = len(peliculas)
suma = 0
mejor = peliculas[0]

for pelicula in peliculas:
    puntaje = int(pelicula["puntaje"])
    suma += puntaje
    if puntaje > int(mejor["puntaje"]):
        mejor = pelicula

promedio = suma / cantidad

print("Cantidad de peliculas:", cantidad)
print(f"Puntaje promedio: {promedio:.1f}")
print("Mejor puntuada:", mejor["titulo"])
