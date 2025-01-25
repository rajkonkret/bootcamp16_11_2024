# unittesty - testy jednostkowe
# pytest - testowanie
# pip install pytest
# Asercja to instrukcja służaca do sprawdzania poprawności założeń w kodzie
# jeśli asercja zwróci True - program kontynuuje działanie, jest ok
# jeśli będzie False - python zgłosi wyjątek AssertionError
# testy jednstkowe pozwalją nam wychwycić niezgodnośc zalożen biznesowych z kodem
# w fazie tworzenia, rozwoju, utrzymania kodu
# uruchomienie testów pytest .\test-122.py
# zmiana katalogu cd nazwa_katalogu
# wyjcie do wyższego katalogu cd ..
from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passed(self):
        self.assertTrue(True)

    def test_uppercase(self):
        assert 'python'.upper() == 'PYTHON'  # sprawdzenie wyniku działania funkcji upper()

    def test_reversed(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]

    def test_always_fail(self):
        self.assertTrue(False)  # AssertionError: False is not true

