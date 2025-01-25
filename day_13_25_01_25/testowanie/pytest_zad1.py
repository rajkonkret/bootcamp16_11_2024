import pytest


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b


def test_addition():
    result = add(2.5, 3.5)
    assert result == 6.0
    assert result == 6


# dwa testy do sprawdzenia funkcji divide()
def test_division():
    assert divide(5, 1) == 5
    assert divide(5, 1) == 5.0


def test_divion_by_two():
    assert divide(6, 2) == 3
    assert divide(6, 2) == 3.0

# sprawdzenie czy dla danych wejściowych (b=0) funkcja rzuci bład ZeroDivisionError
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_division_type():
    assert divide(6, "2") # TypeError

def test_division_type_error():
    with pytest.raises(TypeError):
        divide(10, "2")