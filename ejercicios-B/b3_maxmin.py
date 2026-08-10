puntajes = [120, 45, 300, 80, 210]

mayor = puntajes[0]
menor = puntajes[0]

for p in puntajes:
    if p > mayor:
        mayor = p
    if p < menor:
        menor = p

promedio = sum(puntajes) / len(puntajes)

print("Mayor:", mayor, "Menor:", menor, "Promedio:", promedio)

print("Mayor:", max(puntajes), "Menor:", min(puntajes))
