from ficha import duracion_de


def test_duracion_cuando_la_clave_no_existe():
    pelicula = {"titulo": "the shutter island", "anio": 2010}
    assert duracion_de(pelicula) == "desconocido"


def test_duracion_cuando_la_clave_existe():
    pelicula = {"titulo": "the shutter island", "anio": 2010, "duracion": 138}
    assert duracion_de(pelicula) == 138
    