# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))
sum = 0

if (number > 99) and (number < 1000):
    sum = sum + number % 10
    number = number // 10
    sum = sum + number % 10
    sum = sum + number // 10 
    print(sum)
else:
    print("Неправильный ввод числа!")