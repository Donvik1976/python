# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному
# файлу со словарём. Проверить работу скрипта для случая, когда все файлы
# находятся в разных папках.

from itertools import zip_longest
import sys


def users_hobby_pers(us, hob, per):
    user, hobby = [], []
    with open(us, 'r', encoding='utf-8') as users:
        with open(hob, 'r', encoding='utf-8') as hobbies:
            for line_us in users:
                user.append(line_us.strip().replace(',', ' '))
            for line_hob in hobbies:
                hobby.append(line_hob.strip().split(','))
            if len(user) < len(hobby):
                exit(1)
    with open(per, 'w', encoding='utf-8') as f:
        for line_us, line_hob in zip_longest(user, hobby):
            f.write(f'{line_us}: {line_hob}\n')


x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
users_hobby_pers(x, y, z)

# python task_6_5.py users.csv hobby.csv persons.csv
