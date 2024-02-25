import json
from abc import ABC, abstractmethod
import requests


class APIHHru(ABC):
    """
    Абстрактный класс для работы с API HH.ru
    """

    @abstractmethod
    def get_vacancies(self, vacancies):
        pass


class GetVacansies(APIHHru):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.response = None

    def get_vacancies(self, vacancies):
        """
        Метод для отправки запроса и получения ответа в виде json
        """
        params = {
            'text': vacancies,
            'enable_snippets': "true",
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = requests.get(self.url, params)
        self.response = json.dumps(response.json(), indent=4, ensure_ascii=False)
        return self.response
