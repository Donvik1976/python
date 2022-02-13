duration = int(input('Введите число: '))
# Проверяем секунды
if duration < 60:
    print(f'{duration} сек')
# Проверяем секунды и минуты
elif duration < 60 * 60:
    m = duration // 60
    s = duration % 60
    print(f'{m} мин {s} сек')
# Проверяем секунды, минуты и часы
elif duration < 60 * 60 * 24:
    h = duration // (60 * 60)
    m = duration // 60 % 60
    s = duration % 60
    print(f'{h} час {m} мин {s} сек')
# Проверяем секунды, минуты, часы и дни
else:
    d = duration // (60 * 60 * 24)
    h = duration // (60 * 60) % 24
    m = duration // 60 % 60
    s = duration % 60
    print(f'{d} дн {h} час {m} мин {s} сек')
