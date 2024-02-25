import pytest
from src.hhruapi import GetVacansies


def test_type():
    """Проверяем тип данных возвращаемых функцией get_vacancies"""
    v = GetVacansies()
    assert type(v.get_vacancies('Python')) == str
