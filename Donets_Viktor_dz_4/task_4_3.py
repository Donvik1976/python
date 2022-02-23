# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать
# кроме курса дату, которая передаётся в ответе сервера. Дата должна быть в
# виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных
# лучше использовать в ответе функции?

import datetime

from requests import get


def currency_rates_adv(x):
    rates = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = rates.text
    date_str = content[
               (content.index('Date=') + 6):(content.index('Date=') + 16)]
    date_actual = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
    print(f'Дата курса: {date_actual}')
    x = x.upper()
    if x in content:
        content_rates = content[content.index(x):]
        content_rates = content_rates[:content_rates.index('</Value>')]
        value_str = content_rates[(content_rates.index('<Value>') + 7):]
        value = float(value_str.replace(',', '.'))
        nominal = content_rates[(content_rates.index('<Nominal>') + 9):
                                content_rates.index('</Nominal>')]
        return print(f'Курс {nominal} {x} на {date_actual} составляет '
                     f'{value:.2f} рублей')
    else:
        return print(None)


if __name__ == '__main__':

    currency_rates_adv(input('Введите название валюты(USD, EUR, KZT...): '))

