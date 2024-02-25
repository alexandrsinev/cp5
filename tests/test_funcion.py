import pytest
from src.work_vacancies import WorkVacancies
from src.fuction import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


@pytest.fixture
def vacancies():
    return [WorkVacancies('Back-end разработчик (Odoo framework разработчик)', 'Ташкент', 50000,
                          'Навыки написания технической документации и отчетов о проделанной работе. Знание и навыки работы'
                          'с <highlighttext>Python</highlighttext> 3, Django, Django Rest framework...'
                          ),
            WorkVacancies('Back-end разработчик (Odoo framework разработчик)', 'Москва', 100000,
                          'Навыки написания технической документации и отчетов о проделанной работе. Знание и навыки работы'
                          'с <highlighttext>Python</highlighttext> 3, Django, Django Rest framework...'
                          ),
            WorkVacancies('Back-end разработчик (Odoo framework разработчик)', 'Екатеринбург', 120000,
                          'Навыки написания технической документации и отчетов о проделанной работе. Знание и навыки работы'
                          'с <highlighttext>Python</highlighttext> 3, Django, Django Rest framework...')
            ]


def test_filter_vacancies(vacancies):
    assert filter_vacancies(vacancies, 'Москва') == [vacancies[1]]
    assert filter_vacancies(vacancies, '') == vacancies


def test_get_vacancies_by_salary(vacancies):
    assert get_vacancies_by_salary(vacancies, '50000 - 100000') == [vacancies[0], vacancies[1]]
    assert get_vacancies_by_salary(vacancies, '') == vacancies


def test_sort_vacancies(vacancies):
    assert sort_vacancies(vacancies) == [vacancies[2], vacancies[1], vacancies[0]]


def test_get_top_vacancies(vacancies):
    rez = get_top_vacancies(vacancies, 5)
    assert len(rez) == 3
    rez = get_top_vacancies(vacancies, 2)
    assert len(rez) == 2
