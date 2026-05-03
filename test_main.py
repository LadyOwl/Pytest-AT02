import pytest
from main import count_vowels

def test_only_vowels():

    assert count_vowels("аеёиоуыэюя") == 10
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():

    assert count_vowels("бвгджзклмнпрст") == 0
    assert count_vowels("12345 !@#$%") == 0

def test_mixed_case():

    assert count_vowels("Привет, мир!") == 3
    assert count_vowels("ЭТО ТЕСТ") == 3
    assert count_vowels("aEiOu АЕИОУ") == 5

