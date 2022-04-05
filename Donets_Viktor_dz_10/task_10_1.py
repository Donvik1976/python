# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.Подсказка: матрица — система некоторых
# математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде. Далее реализовать перегрузку метода __add__() для сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и пр.

from itertools import zip_longest


class Matrix:
    def __init__(self, introduced_matrix):
        self.inlet = introduced_matrix

    def __str__(self):
        return '\n'.join(' '.join(map(str, i)) for i in self.inlet)

    def __add__(self, other):
        final = []
        max_el = [0 for i in range(max(len(self.inlet), len(other.inlet)))]
        for el_1, el_2 in zip_longest(self.inlet, other.inlet,
                                      fillvalue=max_el):
            sum_matrix_line = [x + y for x, y in zip_longest(el_1, el_2,
                                                             fillvalue=0)]
            final.append(sum_matrix_line)
        return Matrix(final)


matrix1 = Matrix([[5, 7], [1, 2], [7, 3]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix3 = Matrix([[4, 1], [5, 3], [3, 7]])
print(matrix1, end='\n\n')
print(matrix2, end='\n\n')
print(matrix3, end='\n\n')
print(matrix1 + matrix2 + matrix3)
