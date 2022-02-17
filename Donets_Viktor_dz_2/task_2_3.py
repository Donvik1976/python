#*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят,
# in place). Эта задача намного серьёзнее, чем может сначала показаться.

original_sentence = ['в', '5', 'часов', '17', 'минут', 'температура',
                     'воздуха', 'была', '+5', 'градусов']
i, word_num = 0, 0
print('Осходный список:', original_sentence)
for word in original_sentence:
    if word == '"' or word == word_num:
        continue
    elif word.isdigit():
        original_sentence.insert(i, '"')
        original_sentence[i + 1] = f'{int(word):02}'
        original_sentence.insert(i + 2, '"')
        word_num = original_sentence[i + 1]
        i += 3
    elif word.isalpha():
        i += 1
    else:
        if len(list(word)) < 3:
            original_sentence.insert(i, '"')
            original_sentence[i + 1] = f'{list(word)[0]}' \
                                       f'{int(list(word)[1]):02}'
            original_sentence.insert(i + 2, '"')
            word_num = original_sentence[i + 1]
            i += 3
print('Обработанный список:', original_sentence)

# Первый вариант
print('Первый вариант обработанной строки:', ' '.join(original_sentence))

# Второй вариант
j = 0
print('Второй вариант обработанной строки: ', end='')
while j < len(original_sentence):
    if original_sentence[j] == '"':
        print(''.join([original_sentence[j], original_sentence[j + 1],
                      original_sentence[j + 2]]), end=' ')
        j += 3
    else:
        print(original_sentence[j], end=' ')
        j += 1
