import os.path
import pandas as pd
import wget
from Time import *


class Maintainer(object):
    @staticmethod
    def update_table():
        if os.path.exists('2022.xlsx'):
            os.remove('2022.xlsx')
        url = r'https://docs.google.com/spreadsheets/d/1wrXhwMEwoYbErhQiVAQ27YxbdkwvHWerIa_5-PImags/' \
              r'export?format=xlsx&id=1wrXhwMEwoYbErhQiVAQ27YxbdkwvHWerIa_5-PImags'
        wget.download(url, os.path.curdir)

    # noinspection PyArgumentList
    @staticmethod
    def open_table(path: str = '2022.xlsx'):
        return pd.read_excel(path)[:-2]

    @staticmethod
    def find_soon_day_birthday(table: pd.DataFrame):
        result = list()
        phones = list()
        for person, birthday, phone in zip(table['ФИ'], table['День рождения'], table['Телефон для связи:']):
            birthday = birthday.replace(year=2020)
            if not pd.isna(person):
                if Time.is_soon(Time.current_datetime(), Time.datetime_to_delta(birthday)):
                    result.append(person)
                elif not pd.isna(phone):
                    phones.append(phone)
        return result, tuple(phones)
