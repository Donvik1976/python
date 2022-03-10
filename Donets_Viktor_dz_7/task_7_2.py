# * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта
# со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в
# любом текстовом редакторе «руками» (не программно); предусмотреть возможные
# исключительные ситуации, библиотеки использовать нельзя.
import os


def creation(dir_path, name):
    if '.' not in name:
        if not os.path.exists(os.path.join(dir_path, name)):
            os.mkdir(os.path.join(dir_path, name))
    else:
        if not os.path.isfile(os.path.join(dir_path, name)):
            file = open(os.path.join(dir_path, name), 'w')
            file.close()


with open('config.yaml', 'r', encoding='utf-8') as config:
    for line in config:
        if line.startswith('--'):
            dir_path_0 = os.getcwd()
            dir_name_file_0 = line[2:].strip('\n')
            creation(dir_path_0, dir_name_file_0)

        elif line.startswith('  --'):
            dir_path_1 = os.path.join(os.getcwd(), dir_name_file_0)
            dir_name_file_1 = line[4:].strip('\n')
            creation(dir_path_1, dir_name_file_1)

        elif line.startswith('    --'):
            dir_path_2 = os.path.join(dir_path_1, dir_name_file_1)
            dir_name_file_2 = line[6:].strip('\n')
            creation(dir_path_2, dir_name_file_2)

        elif line.startswith('      --'):
            dir_path_3 = os.path.join(dir_path_2, dir_name_file_2)
            dir_name_file_3 = line[8:].strip('\n')
            creation(dir_path_3, dir_name_file_3)

        elif line.startswith('        --'):
            dir_path_4 = os.path.join(dir_path_3, dir_name_file_3)
            dir_name_file_4 = line[10:].strip('\n')
            creation(dir_path_4, dir_name_file_4)
