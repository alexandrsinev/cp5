import json


class WorkVacancies:
    """
        Класс для обработки ответа с сайта HH.ru и создания списка вакансий
    """
    vacancies_list = []

    def __init__(self, name, city, salary, requirement):
        self.name = name
        self.city = city
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return (f"\nВакансия: {self.name}\n"
                f"Город: {self.city}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirement}\n")

    @classmethod
    def format_vacancies(cls, response):
        """
            Функция возвращает переработанный список вакансий
        """
        vac = json.loads(response)
        for i in vac["items"]:
            if i["salary"] is None:
                i["salary"] = 'Зарплата не указана'
                continue
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                name = i["name"]
                city = i["area"]["name"]
                salary = i["salary"]["from"]
                requirement = i["snippet"]["requirement"]
                instance = cls(name, city, salary, requirement)
                WorkVacancies.vacancies_list.append(instance)

        return cls.vacancies_list


