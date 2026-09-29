def promedio(notas):
    return sum(notas) / len(notas)


def aprobo(notas):
    return promedio(notas) >= 6


if __name__ == "__main__":
    print(promedio([7, 4, 9, 10, 6]))
    print(promedio([10, 8, 9]))
    print(aprobo([7, 4, 9, 10, 6]))
    print(aprobo([4, 5, 3]))
    