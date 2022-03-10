# Написать скрипт, который выводит статис-ку для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а
# значения — общее кол-во файлов (в том числе и в подпапках), размер которых
# не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше
# 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os


def size_test(for_size, start=1, end=10):
    if for_size == 0:
        return 0
    elif 0 < for_size < 1:
        return 10
    while for_size not in range(start, end):
        if for_size not in range(start, end):
            start *= 10
            end *= 10
    return end


folder = os.getcwd()
#folder = r'C:/Users/vdone/PycharmProjects/main_course/Donets_Viktor'
size_files = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        size_key = size_test(os.stat(os.path.join(root, file)).st_size)
        if size_key in size_files:
            size_files[size_key] += 1
        else:
            size_files[size_key] = 1
print(dict(sorted(size_files.items(), key=lambda x: x[0])))
