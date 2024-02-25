def filter_vacancies(vacancies_list, city):
    """
    Функция для сортировки вакансий по городу
    """
    filtered_vacancies = []
    if not city:
        return vacancies_list
    else:
        for vacancy in vacancies_list:
            if vacancy.city == city:
                filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
        Функция для сортировки вакансий по диапазону зарплаты
    """
    ranged_vacancies = []
    if salary_range == '':
        return filtered_vacancies
    else:
        salary_range = salary_range.split()
        for vacancy in filtered_vacancies:
            if int(salary_range[0]) <= vacancy.salary <= int(salary_range[2]):
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    """
        Функция для сортировки вакансий по величине зарплаты
    """
    s_vac = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    return s_vac


def get_top_vacancies(sorted_vac, top_n):
    """
        Функция возвращае количество вакансий которое запросил пользователь
    """
    if top_n > len(sorted_vac):
        return sorted_vac
    return sorted_vac[0: top_n]


#v = GetVacansies()
#l = v.get_vacancies('Python')
#l1 = WorkVacancies.format_vacancies(l)
#f = filter_vacancies(l1, 'Москва')
#for i in f:
    #print(i)
