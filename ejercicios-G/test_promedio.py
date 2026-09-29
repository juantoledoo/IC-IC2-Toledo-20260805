from funciones import promedio


def test_promedio_de_notas():
    assert promedio([7, 4, 9, 10, 6]) == 7.2


def test_promedio_de_lista_vacia_devuelve_cero():
    assert promedio([]) == 0


# G2: test que falla a propósito, comentado después de leer el error de pytest.
# def test_que_falla_a_proposito():
#     assert promedio([7, 4, 9, 10, 6]) == 8
