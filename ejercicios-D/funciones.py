def promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def aprobo(notas, minimo=6):
    return promedio(notas) >= minimo


def estadisticas(notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas),
    }


def reporte(notas):
    stats = estadisticas(notas)
    return f"Promedio: {stats['promedio']:.1f} | Máximo: {stats['maximo']} | Mínimo: {stats['minimo']}"


if __name__ == "__main__":
    print(promedio([7, 4, 9, 10, 6]))
    print(promedio([10, 8, 9]))
    print(promedio([]))
    print(aprobo([7, 4, 9, 10, 6]))
    print(aprobo([4, 5, 3]))
    print(aprobo([5, 6, 7]))
    print(aprobo([5, 6, 7], minimo=7))
    print(estadisticas([7, 4, 9, 10, 6]))
    print(reporte([7, 4, 9, 10, 6]))
    