alumnos = list(range(1, 31))

pares = []
impares = []

for numero in alumnos:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Pares:", len(pares))
print("Impares:", len(impares))
