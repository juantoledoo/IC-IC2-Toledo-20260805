from pathlib import Path

ruta = Path(__file__).parent / "peliculas.csv"

with open(ruta, encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
        