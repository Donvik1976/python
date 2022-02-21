# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в
# качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в
# котором ключи — первые буквы фамилий, а значения — словари, реализованные по
# схеме предыдущего задания и содержащие записи, в которых фамилия начинается
# с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
#                   "Илья Иванов", "Анна Савельева")
# {
# "А": {"П": ["Петр Алексеев"]},
# "И": {"И": ["Илья Иванов"]},
# "С": {"И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"]}
# }
#
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    for word in args:
        first_name, last_name = word.split()
        wordbook_name = {}
        if last_name[0] in wordbook_full:
            if first_name[0] in wordbook_full[last_name[0]]:
                wordbook_full[last_name[0]][first_name[0]].append(word)
        else:
            wordbook_name[first_name[0]] = [word]
            wordbook_full.setdefault(last_name[0], wordbook_name)
    return


wordbook_full = {}
thesaurus_adv('Иван Сергеев', 'Инна Серова ', 'Петр Алексеев', 'Илья Иванов',
              'Анна Савельева', 'Павел Антипин', 'Олег Муллер')

# Вывод полученного словаря
print(wordbook_full)

# Вывод отсорированного словаря
wordbook_full_lst = list(wordbook_full.keys())
wordbook_full_lst.sort()
for key in wordbook_full_lst:
    print(f'{key}: {wordbook_full[key]}')
