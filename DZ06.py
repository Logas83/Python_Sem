# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

def Sum(num):
    sum = 0
    sum = sum + num % 10
    num = num // 10
    sum = sum + num % 10
    sum = sum + num // 10 
    return sum

number = input("Введите шестизначное число: ")
if (len(number) > 5) and (len(number) < 7):
    firstNumber = int(number[3:])
    secondNumber = int(number[:3])
    if Sum(firstNumber) == Sum(secondNumber):
        print("yes")
    else:
        print("no")
else:
    print("Неправильный ввод числа!")