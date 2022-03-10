# Написать скрипт, создающий стартер (заготовку) для проекта со следующей
# структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
# можно было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах
# (добавлять детали)?

import os

project_dir = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for key in project_dir.keys():
    dir_name = key
    for i in range(len(project_dir[dir_name])):
        dir_patch = os.path.join(dir_name, project_dir[dir_name][i])
        if not os.path.exists(dir_name):
            os.makedirs(dir_patch)
        else:
            if not os.path.exists(dir_patch):
                os.makedirs(dir_patch)
