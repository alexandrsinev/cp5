from src.work_vacancies import WorkVacancies
import pytest


@pytest.fixture
def vacancy():
    return WorkVacancies("Программист Python", "Екатеринбург", "54000",
                         "Применять паттерны проектирования...")


def test_constructor(vacancy):
    assert vacancy.name == "Программист Python"
    assert vacancy.city == "Екатеринбург"
    assert vacancy.salary == "54000"
    assert vacancy.requirement == "Применять паттерны проектирования..."
