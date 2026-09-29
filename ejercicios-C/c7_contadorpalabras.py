frase = "el gato ve al gato y el gato ve al perro"

palabras = frase.split()

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)
