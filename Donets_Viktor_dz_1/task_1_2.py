#Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):

odd_numbers = []
number = 1
while number < 1000:
    if number % 2:
        odd_numbers.append(number ** 3)
        number += 1
    else:
        number += 1
print('Список из кубов нечетных чисел =', odd_numbers)


# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так
# как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать
# только арифметические операции!

sum_odd = 0
i = 0
while i < len(odd_numbers):
    numeric = odd_numbers[i]
    sum_numeric = 0
    while numeric != 0:
        sum_numeric += numeric % 10
        numeric = (numeric - numeric % 10) // 10
    if not sum_numeric % 7:
        sum_odd += odd_numbers[i]
    i += 1
print('a)', sum_odd)


# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
# из этого списка, сумма цифр которых делится нацело на 7.

#Создадим новый список из odd_numbers с элементами на 17 больше
new_numbers = []
j = 0
while j < len(odd_numbers):
    new_numbers.append(odd_numbers[j] + 17)
    j += 1
print('Новый список из пункта b) =', new_numbers)

#Прогнав новый список через алгоритм из пункта a), мы получим новую сумму

sum_new = 0
i = 0
while i < len(new_numbers):
    numeric = new_numbers[i]
    sum_numeric = 0
    while numeric != 0:
        sum_numeric += numeric % 10
        numeric = (numeric - numeric % 10) // 10
    if not sum_numeric % 7:
        sum_new += new_numbers[i]
    i += 1
print('b)', sum_new)


# c)  Решить задачу под пунктом b, не создавая новый список.

sum_new_another = 0
i = 0
while i < len(odd_numbers):
    numeric = odd_numbers[i] + 17
    sum_numeric = 0
    while numeric != 0:
        sum_numeric += numeric % 10
        numeric = (numeric - numeric % 10) // 10
    if not sum_numeric % 7:
        sum_new_another += odd_numbers[i] + 17
    i += 1
print('c)', sum_new_another)




