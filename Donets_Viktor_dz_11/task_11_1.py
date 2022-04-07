# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, format_date):
        self.format_date = format_date

    @classmethod
    def extracts(cls, format_date):
        date_lst = [int(x) for x in format_date.split('-')]
        valid = Date.validator(date_lst)
        if not valid[0]:
            print(valid[1])
        else:
            print(f'{valid[1]} Число-{date_lst[0]}, месяц-{date_lst[1]}, '
                  f'год-{date_lst[2]}')

    @staticmethod
    def validator(date_lst):
        if 1 > date_lst[0] or date_lst[0] > 31:
            return [False, 'Число должно быть от 1 до 31']
        elif date_lst[1] > 12:
            return [False, 'Месяц должен быть от 1 до 12']
        elif date_lst[2] > 2022:
            return [False, 'Год не может быть больше 2022']
        else:
            return [True, 'Все хорощо!']


Date.extracts('23-04-1976')
print('*' * 50)
Date.extracts('32-04-1976')
print('*' * 50)
Date.extracts('23-13-1976')
print('*' * 50)
Date.extracts('23-12-2023')
