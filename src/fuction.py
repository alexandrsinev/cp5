from src.hhruapi import GetVacansies
from src.work_vacancies import WorkVacancies
import psycopg2

company_name_list = ['Тинькофф', 'Bell Integrator', 'ООО JSA Group', 'IDF Technology', 'ТОО Autodata', 'ReSpec',
                     'ДиБиЭс Технологии', 'ООО Скиллтеллект', 'InfiNet Wireless', 'ООО 24Н Софт']
conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='1335555',
        host='localhost',
        port='5432'
    )

def get_company_name(vacancies_list, companies):
    company_name_vacancies_list = []
    for i in vacancies_list:
        i_dict = vars(i)
        if i_dict["company_name"] in company_name_list:
            company_name_vacancies_list.append(i_dict)
    return company_name_vacancies_list

company_name_vl = get_company_name(vacancies_list, company_name_list)
def create_bd():
def filling_bd():
    vacancies_data = []
    for i in company_name_vl:
        rez = (i)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("insert into employees values(%s, %s, %s, %s, %s, %s)", vacancies_data)
    finally:
        conn.close()


v = GetVacansies()
l = v.get_vacancies()
l1 = WorkVacancies.format_vacancies(l)
f = get_company_name(l1)
# for i in f:
# print(i)
