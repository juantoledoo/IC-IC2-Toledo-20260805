lecturas = [10, 12, 14, 11, 13, 15, 20, 18, 16, 19]

promedios = []

for i in range(len(lecturas) - 2):
    ventana = lecturas[i:i+3]
    promedio_ventana = sum(ventana) / len(ventana)
    promedios.append(promedio_ventana)

print("Lecturas:", lecturas)
print("Promedios moviles:", promedios)
print("Cantidad de lecturas:", len(lecturas))
print("Cantidad de promedios:", len(promedios))
