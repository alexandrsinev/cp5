from abc import ABC, abstractmethod
from config import FILE


class Saver(ABC):
    """
        Абстрактный класс для сохранения данных о вакансиях
    """

    @abstractmethod
    def save_in_json(self, vacancies):
        pass


class SaverData(Saver):

    def save_in_json(self, vacancies):
        """
            Функция записывает вакансии в json файл
        """
        with open(FILE, 'w', encoding='utf-8') as file:
            file.write(vacancies)
