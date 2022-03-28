# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и
# возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их
# в регулярном выражении; имеет ли смысл в данном случае использовать функцию
# re.compile()?

import re


def email_parse(email_address):
    dict_parse['username'] = re.findall(r"^[^@]+", email_address)[0]
    if re.findall(r"@(\S+\.\S+)", email_address):
        dict_parse['domain'] = re.findall(r"@(\S+\.\S+)", email_address)[0]
    else:
        raise ValueError(f'wrong email: {email_address}')


dict_parse = {}
email_parse(input('Введите адреc: '))
print(dict_parse)
