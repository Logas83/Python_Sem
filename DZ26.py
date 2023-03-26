# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def Exponentiation(num, deg):
    if deg == 1:
        return num
    
    return num * Exponentiation(num, deg - 1)

number = int(input("Введите число: "))
degree = int(input("Введите степень: "))

print(Exponentiation(number, degree))