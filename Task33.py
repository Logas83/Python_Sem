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

# def min_max_serch(input_list):
#     return min(input_list), max(input_list)


# def min_max_replace(start_list, copy=True):
#     if copy:
#         start_list = start_list.copy()
#         min_el, max_el = min_max_serch(start_list)
#     while max_el in start_list:
#         max_index = start_list.index(max_el)
#         start_list[max_index] = min_el
#     return start_list



# start_list = [1, 4, 3, 5, 4]
# print(min_max_replace(start_list))