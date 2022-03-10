# * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в
# виде словаря, в котором ключи те же, а значения — кортежи вида
# (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где
# запустили скрипт.
import os
import json


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
        extension = file[file.rfind('.') + 1:]
        if size_key in size_files and extension in size_files[size_key][1]:
            size_files[size_key][0] += 1
        elif size_key in size_files and extension not in size_files[size_key][1]:
            size_files[size_key][0] += 1
            size_files[size_key][1].append(extension)
        else:
            size_files[size_key] = [1, [extension]]

for key, value in size_files.items():
    size_files[key] = tuple(value)
size_files_sort = dict(sorted(size_files.items(), key=lambda x: x[0]))
print(size_files_sort)

with open('_summary.json', 'w', encoding='utf-8') as f:
    json.dump(size_files_sort, f)
