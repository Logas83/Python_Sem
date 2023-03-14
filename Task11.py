# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

# Input:     5
# Output:  6
"""
a = int(input("Введите а: "))
first = 0
second = 1

if a == 0:
    print(1)
elif a == 1:
    print(2)

count = 2

while second < a:
    buffer = first + second
    first = second
    second = buffer
    count += 1
if second == a:
    print(count)
else:
    print(-1)
"""

number = int(input("Введите число: "))
f1 = f2 = 1
n = 3 # число больше 1
while number > f2 :
    f1, f2 = f2, f1 + f2
    n +=1
print(n if number == f2 else '-1')