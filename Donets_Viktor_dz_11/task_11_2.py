#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class ZeroDivision(ZeroDivisionError):
    pass


arg_1 = int(input('Введите первое число: '))
while True:
    arg_2 = int(input('Введите второе число: '))
    try:
        if arg_2 == 0:
            raise ZeroDivision(arg_2)
    except ZeroDivision as zd:
        print(f'Делить на {zd} нельзя!')
    else:
        print(arg_1 / arg_2)
        break
