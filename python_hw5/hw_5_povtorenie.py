import random

#1 Написать скрипт, который в создаст список целых чисел.

integer_list = list(range(70))
print("integer_list =", integer_list)

#2 Написать скрипт, который в создаст список целых чётных чисел

even_integer_list = list(range(0, 70, 2))
print("even_integer_list =", even_integer_list)

#3 Написать скрипт, который в создаст список целых нечётных чисел
odd_integer_list = list(range(1, 70, 2))
print("odd_integer_list =", odd_integer_list)

#4 Написать скрипт, который из списка целых чисел выведет чётные числа.
even_list = []
for i in integer_list:
    if i % 2 == 0:
        even_list.append(i)
print("even_list =", even_list)

#5 Написать скрипт, который из списка целых чисел выведет нечётные числа.
odd_list = []
for i in integer_list:
    if i % 2 != 0:
        odd_list.append(i)
print("odd_list =", odd_list)

#6 Написать скрипт, который из списка целых чисел выведет
# чётные числа которые делятся на 5 без остатка.
even_five_list = []
for i in integer_list:
    if i % 2 == 0 and i % 5 == 0:
        even_five_list.append(i)
print("even_five_list =", even_five_list)
