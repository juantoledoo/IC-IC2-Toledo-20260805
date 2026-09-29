import csv
from pathlib import Path

genero_elegido = "ciencia ficcion"

carpeta = Path(__file__).parent
ruta_entrada = carpeta / "peliculas.csv"
ruta_salida = carpeta / "filtradas.csv"

filtradas = []

with open(ruta_entrada, encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    columnas = lector.fieldnames
    for fila in lector:
        if fila["genero"] == genero_elegido:
            filtradas.append(fila)

with open(ruta_salida, "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(filtradas)

print(f"Se guardaron {len(filtradas)} peliculas de {genero_elegido} en filtradas.csv")
