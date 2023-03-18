# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [4, 5, 1, 2, 3]

str1 = input("Введите числа через пробел: ")
list_str = str1.split(sep=' ')

list_int = [int(i) for i in list_str]

print(f"Вы ввели следующие цифры: {list_int}")

k = int(input("Введите количество сдвигов: "))

count = 0

while count < k:
    list_int.append(list_int.pop(0))
    count += 1

print(list_int)