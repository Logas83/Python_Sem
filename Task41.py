# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел. Каждое число вводится с новой строки.


# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0

# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

def CreateList(size):
    new_list = []

    for i in range(size):
        new_list.append(int(input("Введите число: ")))

    return new_list


size_list1 = int(input("Введите размер списка: "))
list1 = CreateList(size_list1)

count = 0

for i in range(1, len(list1) - 1):
    if (list1[i] > list1[i - 1]) and (list1[i] > list1[i + 1]):
        count += 1

print(count)