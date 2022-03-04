# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные
# об их хобби. Известно, что при хранении данных используется принцип: одна
# строка — один пользователь, разделитель между значениями — запятая. Написать
# код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если
# наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что
# объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

# with open('users.csv', 'w', encoding='utf-8') as f:
#     f.write(
#         'Иванов, Иван, Иванович\n'
#         'Петров,Петр,Петрович\n'
#         'Сидоров,Макар,Федорович\n'
#         'Кротов,Самсон,Ильич'
#     )
#
# with open('hobby.csv', 'w', encoding='utf-8') as f:
#     f.write(
#         'скалолазание,охота\n'
#         'горные лыжи\n'
#         'настольный теннис,футбол'
#     )

import json
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        user = users.read().strip().replace(',', ' ').split('\n')
        hobby = hobbies.read().strip().replace(',', ', ').split('\n')
        if len(user) < len(hobby):
            exit(1)

with open('persons.csv', 'w', encoding='utf-8') as f:
    person = json.dumps({us: hob for us, hob in zip_longest(user, hobby)},
                        ensure_ascii=False)
    f.write(person)

# print(user)
# print(hobby)
print(person)
