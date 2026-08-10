ficha1 = {"titulo": "Peaky Blinders: El hombre inmortal", "anio": 2026}
ficha2 = {"puntaje": 8, "anio": 2024}

combinado_1 = ficha1 | ficha2
combinado_2 = ficha2 | ficha1

print("ficha1 | ficha2 ->", combinado_1)
print("ficha2 | ficha1 ->", combinado_2)