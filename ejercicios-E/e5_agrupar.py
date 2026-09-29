import csv
from pathlib import Path

ruta = Path(__file__).parent / "peliculas.csv"

puntajes_por_genero = {}

with open(ruta, encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        genero = fila["genero"]
        if genero not in puntajes_por_genero:
            puntajes_por_genero[genero] = []
        puntajes_por_genero[genero].append(int(fila["puntaje"]))

promedios = {}

for genero, puntajes in puntajes_por_genero.items():
    promedios[genero] = sum(puntajes) / len(puntajes)

print(promedios)
