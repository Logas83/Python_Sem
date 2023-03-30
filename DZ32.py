# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).

import random


def CreateRndArray(start, finish, step, size):
    return [random.randrange(start, finish, step) for i in range(size)]


list1 = CreateRndArray(1, 50, 1, 7)
print(list1)

min_position, max_position = 10, 20

for i in list1:
    if i > min_position and i < max_position:
        print(list1.index(i), end=" ")