from src.hhruapi import APIHHru, GetVacansies
from src.work_vacancies import WorkVacancies
from src.fuction import *
from src.saver import SaverData

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = GetVacansies()


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")

    response = hh_api.get_vacancies(search_query)
    vacancies_list = WorkVacancies.format_vacancies(response)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите город в котором ищите вакансию: ")
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    for i in top_vacancies:
        print(i)
    return response


if __name__ == "__main__":
    vacancy = user_interaction()
    # Сохранение информации о вакансиях в файл
    json_saver = SaverData()
    json_saver.save_in_json(vacancy)
