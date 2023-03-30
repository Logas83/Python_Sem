# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива.

# Ввод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# (каждое число вводится с новой строки)

# Вывод: 3 3 2 12

def CreateList(size):
    new_list = []

    for i in range(size):
        new_list.append(int(input("Введите число: ")))

    return new_list


size_list1 = int(input("Введите размер первого списка: "))
list1 = CreateList(size_list1)
print()
size_list2 = int(input("Введите размер второго списка: "))
list2 = CreateList(size_list2)

set1 = set(list1).difference(set(list2))

for i in list1:
    if i in set1:
        print(i, end=" ")