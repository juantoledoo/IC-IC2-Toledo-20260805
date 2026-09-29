from funciones import estadisticas


def test_estadisticas_devuelve_las_tres_claves_con_sus_valores():
    resultado = estadisticas([7, 4, 9, 10, 6])
    assert set(resultado.keys()) == {"promedio", "maximo", "minimo"}
    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4
    