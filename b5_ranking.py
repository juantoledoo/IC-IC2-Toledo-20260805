puntajes = [120, 45, 300, 80, 210]

ordenado_copia = sorted(puntajes, reverse=True)
print("Copia ordenada:", ordenado_copia)
print("Original (sigue igual):", puntajes)

puntajes.sort(reverse=True)
print("Original despues de .sort():", puntajes)
