# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

list_size = int(input("Введите размер массива: "))

list1 = list()

for i in range(list_size):
    list1.append(int(input("Введите элемент массива: ")))

number = int(input("Введите число для сравнения: "))

value = 0
min_value = number - list1[0]
result = 0

for i in range(1, len(list1)):
    value = number - list1[i]
    if value < 0:
        value = value * (-1)
    if value < min_value:
        result = list1[i]

print(f"Самый близкий по величине элемент к заданному числу {number}: {result}")