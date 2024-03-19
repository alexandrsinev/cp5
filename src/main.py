from src.hhruapi import APIHHru, GetVacansies
from src.work_vacancies import WorkVacancies
from src.fuction import *
from src.saver import SaverData

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = GetVacansies()

company_name_list = ['Тинькофф', 'Bell Integrator', 'ООО JSA Group', 'IDF Technology', 'ТОО Autodata', 'ReSpec',
                     'ДиБиЭс Технологии', 'ООО Скиллтеллект', 'InfiNet Wireless', 'ООО 24Н Софт']

    response = hh_api.get_vacancies()
    vacancies_list = WorkVacancies.format_vacancies(response)
    def get_company_name(vacancies_list):
        company_name_vacancies_list = []
        for i in vacancies_list:
            i_dict = vars(i)
            if i_dict["company_name"] in company_name_list:
                company_name_vacancies_list.append(i_dict)
        return company_name_vacancies_list

if __name__ == "__main__":
