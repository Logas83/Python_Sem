# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def ReplacingDigits(array):
    max_num = max(array)
    min_num = min(array)

    for i in range(len(array)):
        if array[i] == max_num:
            array[i] = min_num
    
    return array


size = int(input("Введите количество цифр: "))

count = 1
list1 = []

while count <= size:
    list1.append(int(input(f"Введите {count} число: ")))
    count += 1

print(ReplacingDigits(list1))