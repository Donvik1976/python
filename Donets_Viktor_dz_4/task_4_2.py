# Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
# отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно смотреть содержимое ответа. Можно ли, используя
# только методы класса str, решить поставленную задачу? Функция должна
# возвращать результат числового типа, например float. Подумайте: есть ли смысл
# для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента
# передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать
# работу функции не зависящей от того, в каком регистре был передан аргумент? В
# качестве примера выведите курсы доллара и евро.

from requests import get


def currency_rates(x):
    x = x.upper()
    if x in content:
        content_rates = content[content.index(x):]
        content_rates = content_rates[:content_rates.index('</Value>')]
        value_str = content_rates[(content_rates.index('<Value>') + 7):]
        value = float(value_str.replace(',', '.'))
        nominal = content_rates[(content_rates.index('<Nominal>') + 9):
                                content_rates.index('</Nominal>')]
        return print(f'Курс {nominal} {x} составляет {value:.02f} рублей')
    else:
        return print(None)


rates = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = rates.text
currency_rates('USD')
currency_rates('EUR')
currency_rates('kzt')
currency_rates('USB')
