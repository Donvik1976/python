# Представлен список чисел. Необходимо вывести те его элементы, значения
# которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке. Подумайте,
# как можно сделать оптимизацию кода по памяти, по скорости.
import sys
from time import perf_counter


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Вариант 1
start = perf_counter()
result = []
i = 0
while i < len(src) + 1:
    if i + 1 < len(src) and src[i + 1] > src[i]:
        result.append(src[i + 1])
        i += 1
    else:
        i += 1

print(result, perf_counter() - start, sys.getsizeof(result))

# Вариант 2
start = perf_counter()
result = []
i = 0
for i in range(len(src)):
    if i + 1 < len(src) and src[i + 1] > src[i]:
        result.append(src[i + 1])
        i += 1
    else:
        i += 1

print(result, perf_counter() - start, sys.getsizeof(result))

# Вариант 3
start = perf_counter()
result = ([src[i + 1] for i in range(len(src))
           if i + 1 < len(src) and src[i + 1] > src[i]])
print(result, perf_counter() - start, sys.getsizeof(result))

# Вариант 4
start = perf_counter()
result = (src[i + 1] for i in range(len(src))
          if i + 1 < len(src) and src[i + 1] > src[i])

print(result, perf_counter() - start, sys.getsizeof(result))

# Вариант 5
start = perf_counter()
result = [j for i, j in zip(src, src[1:]) if j > i]
print(result, perf_counter() - start, sys.getsizeof(result))

# По памяти и скорости оптимизируется только в варианте 4, так как создается
# не список, а генератор