from funciones import aprobo


def test_aprobo_cuando_el_promedio_alcanza():
    assert aprobo([7, 4, 9, 10, 6]) is True


def test_no_aprobo_cuando_el_promedio_no_alcanza():
    assert aprobo([4, 5, 3]) is False


def test_aprobo_en_el_limite_de_6():
    assert aprobo([5, 6, 7]) is True
    