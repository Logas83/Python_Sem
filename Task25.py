# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Ouput: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

s = ("a a a b c a a d c d d").split()

dict = {}

for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end=' ')
    else:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
