# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# Input:       5
# Output:    120

factorial = int(input("Введите число факториала: "))
count = 1
result = 1

while count <= factorial:
    result *= count
    count += 1

print(result)