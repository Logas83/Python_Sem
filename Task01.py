# За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750

# Output:
# 2

#print((m := int(input())) // (n := int(input())) + (m % n > 0))

import math
a = int(input('Введите количество километров за день: '))
b = int(input('Введите маршрут км: '))
print(math.ceil(b / a))