# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input("Введите первый элемент массива: "))
step = int(input("Введите шаг прогресии: "))
size_array = int(input("Введите размер массива: "))

list1 = [size_array]
list1[0] = first_element
count = 1

while count < size_array:
    first_element += step
    list1.append(first_element)
    count += 1

print(list1)

# a1 = int(input())
# d = int(input())
# n = int(input())

# for i in range(n):
#     print(a1 + i * d)