frase = "le quieren venir a hablar de kiosco al maxi"

palabras = frase.split()

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)