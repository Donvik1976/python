# Создать структуру файлов и папок, как написано в задании 2 (при помощи
# скрипта или «руками» в проводнике). Написать скрипт, который собирает все
# шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что
# html-файлы расположены в родительских папках (они играют роль пространств
# имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.
import os
import shutil


def transferal(dir_temp, temp_0):
    for i in os.listdir(dir_temp):
        if ('.' not in i) \
                and (not os.path.exists(os.path.join(temp_0, i))):
            os.mkdir(os.path.join(temp_0, i))
            new_dir_temp = os.path.join(dir_temp, i)
            new_temp_0 = os.path.join(temp_0, i)
            transferal(new_dir_temp, new_temp_0)
        else:
            shutil.copy2(os.path.join(dir_temp, i), os.path.join(temp_0, i))


my_project = os.path.join(os.getcwd(), 'my_project')
if not os.path.exists(os.path.join(os.getcwd(), 'my_project', 'templates')):
    os.mkdir(os.path.join(my_project, 'templates'))
else:
    shutil.rmtree(os.path.join(my_project, 'templates'))
    os.mkdir(os.path.join(my_project, 'templates'))

for root, dirs, files in os.walk(my_project):
    for directory in dirs:
        if directory == 'templates' \
                and len(os.listdir(os.path.join(root, directory))) > 0:
            transferal(os.path.join(root, directory),
                       os.path.join(my_project, 'templates'))
