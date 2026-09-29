import pytest

from funciones import aprobo


@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([7, 4, 9, 10, 6], True),
        ([4, 5, 3], False),
        ([5, 6, 7], True),
    ],
)
def test_aprobo(notas, esperado):
    assert aprobo(notas) is esperado
    