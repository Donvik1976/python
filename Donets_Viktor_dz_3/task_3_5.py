# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
# повторы слов в шутках (когда каждое слово можно использовать только в одной
# шутке)? Сможете ли вы сделать аргументы именованными?


from random import randrange


def get_jokes(number_joke, flag='True'):
    """
    Функция для создания шуток

    :Можно сделать с повторами слов установив флажок True
    :Можно сделать без повторов слов, но ограниченноне колличество
                                    установив флажок False
    """

    jokes, i = [], 0
    if flag == 'True':
        while i < number_joke:
            jokes.append(f'{nouns[randrange(len(nouns))]} '
                         f'{adverbs[randrange(len(adverbs))]} '
                         f'{adjectives[randrange(len(adjectives))]}')
            i += 1
        return print(jokes)
    elif flag == 'False':
        if number_joke <= min(len(adverbs), len(nouns), len(adjectives)):
            while i < number_joke :
                noun = nouns[randrange(len(nouns))]
                nouns.remove(noun)
                adverb = adverbs[randrange(len(adverbs))]
                adverbs.remove(adverb)
                adjective = adjectives[randrange(len(adjectives))]
                adjectives.remove(adjective)
                jokes.append(f'{noun} {adverb} {adjective}')
                i += 1
            return print(jokes)
        else:
            print('Закажите меньшее количество шуток')


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(int(input('Веедите количество шуток: ')),
          input('Введите флаг True - с повторами, False - без: '))
