# * (вместо 6) Добавить возможность редактирования данных при помощи
# отдельного скрипта: передаём ему номер записи и новое значение. При этом
# файл не должен читаться целиком — обязательное требование. Предусмотреть
# ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys


def change_sales(lin, sales):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        with open('additional.csv', 'w+', encoding='utf-8') as addit:
            for string, reader in enumerate(f, start=1):
                if lin == string:
                    # Честно говоря отсюда я подсмотрел у Вас, ни как не мог
                    # понять как сделать, оказывается нужно было создать
                    # новый файл и перезаписать из него в конечный.
                    addit.write(f'{sales}\n')
                else:
                    addit.write(reader)
            if lin > string:
                exit(1)
            f.seek(0)
            addit.seek(0)
            for line in addit:
                f.write(line)


x, y = sys.argv[1:]
change_sales(int(x), int(y))
