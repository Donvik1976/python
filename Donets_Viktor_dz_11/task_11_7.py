# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
# класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, x, y, action=None):
        self.x = x
        self.y = y
        self.z = action

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y, 'Сумма')

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - (self.y * other.y),
                             self.x * other.y + (self.y * other.x),
                             'Произведение')

    def __str__(self):
        if self.z and self.y == 0:
            return f'{self.z} = {self.x}'
        elif self.z:
            return f'{self.z} = {self.x} + ({self.y} * i)'
        elif self.y == 0:
            return f'z = {self.x}'
        else:
            return f'z = {self.x} + ({self.y} * i)'


z_1 = ComplexNumber(5, 3)
z_2 = ComplexNumber(2, -1)
print(z_1)
print(z_2)
print('*' * 25)
print(z_1 + z_2)
print(z_1 * z_2)
print('*' * 25)
z_3 = ComplexNumber(-2, 0)
print(z_3)
print('*' * 25)
print(z_1 + z_2 + z_3)
print(z_1 * z_2 * z_3)
