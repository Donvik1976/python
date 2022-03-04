# * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах
# превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие
# файлы, это просто задел на будущее проекта). Также реализовать парсинг данных
# из файлов — получить отдельно фамилию, имя и отчество для пользователей и
# название каждого хобби: преобразовать в какой-нибудь контейнерный тип
# (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие
# могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
# полученные в результате парсинга.

from itertools import zip_longest

user, hobby = [], []
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        for line_us in users:
            user.append(line_us.strip().replace(',', ' '))
        for line_hob in hobbies:
            hobby.append(line_hob.strip().split(','))
        if len(user) < len(hobby):
            exit(1)

with open('persons.csv', 'w', encoding='utf-8') as f:
    for us, hob in zip_longest(user, hobby):
        f.write(f'{us}: {hob}\n')
