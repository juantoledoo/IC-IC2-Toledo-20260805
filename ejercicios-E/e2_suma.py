import csv
from pathlib import Path

ruta = Path(__file__).parent / "peliculas.csv"

total = 0

with open(ruta, encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        total += int(fila["puntaje"])

print("Suma de puntajes:", total)
