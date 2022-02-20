import random
from random import randint
import numpy as np
import names

# 1 На"писать скрипт, который в создаст список целых чисел.
print("task 1")
integer_list = list(range(70))
print("integer_list =", integer_list)

# 2 Написать скрипт, который в создаст список целых чётных чисел
print("task 2")
even_integer_list = list(range(0, 70, 2))
print("even_integer_list =", even_integer_list)

# 3 Написать скрипт, который в создаст список целых нечётных чисел
print("task 3")
odd_integer_list = list(range(1, 70, 2))
print("odd_integer_list =", odd_integer_list)

# 4 Написать скрипт, который из списка целых чисел выведет чётные числа.
print("task 4")
even_list = []
for i in integer_list:
    if i % 2 == 0:
        even_list.append(i)
print("even_list =", even_list)

# 5 Написать скрипт, который из списка целых чисел выведет нечётные числа.
print("task 5")
odd_list = []
for i in integer_list:
    if i % 2 != 0:
        odd_list.append(i)
print("odd_list =", odd_list)

# 6 Написать скрипт, который из списка целых чисел выведет
# чётные числа которые делятся на 5 без остатка.
print("task 6")
even_five_list = []
for i in integer_list:
    if i % 2 == 0 and i % 5 == 0:
        even_five_list.append(i)
print("even_five_list =", even_five_list)

# 7 Написать скрипт, который
# из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
print("task 7")
count_five_list = []
for i in integer_list:
    if i % 2 == 0 and i % 5 == 0:
        count_five_list.append(i)
print("count_five_list", len(count_five_list))

# 8 Написать скрипт, который в создаст список целых рандомных чисел.
print("task 8")
generator = [randint(1, 70) for i in range(70)]
print("random_generator =", generator)

# 9 Написать функцию которая,
# получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
print("task 9")


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


print("list by 5 elements =", split(odd_integer_list, 5))

# 10 Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка,
# список чётных и список нечётных чисел.
print("task 10")


# Нарезка последовательностей поддерживает не только указание
# начального и конечного значения, но и шага (или шага);
# [::2] выбирает каждое второе значение, начиная с 0,
# [1::2] -каждое значение, начиная с 1.

def lists_split_odd_even():
    lists2 = list(range(70));
    even, odd = lists2[::2], lists2[1::2]
    return print("even list =", even, '\n', "odd list =", odd)


lists_split_odd_even()
print("+++++++++++++++++++++++++++=")


def split_even_odd(lists):
    evenlist = []
    oddlist = []
    for i in lists:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even lists:", evenlist)
    print("Odd lists:", oddlist)


split_even_odd(integer_list)
print("+++++++++++++++++++++++++++=")

# 11 Написать скрипт, который сгенерирует список под названием
# 5_stars из списков по 5 элементов целых чисел.
print("task 11")
five_stars = [[k * j for k in range(0, 5)] for j in range(0, 5)]
print("five_stars list =", five_stars)

# 12 Написать скрипт, который выведет список из сумм
# каждого внутреннего списка из 5_stars

# При этом используется комбинация zip и * для распаковки списка,
# а затем архивирование элементов в соответствии с их индексом.
# Затем вы используете понимание списка,
# чтобы перебрать группы похожих индексов, суммируя их и возвращаясь в их «исходную» позицию.
print("task 12")
sum_lists = [sum(l) for l in zip(*five_stars)]
print("sum lists =", sum_lists)

# 13 Написать функцию, которая на вход получает список 5_stars,
# а вернёт 2 списка. В одном списке внутренние списки из 5_stars
# сумма чисел которых >= 100, а другой сумма чисел которых < 100.
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”
print("task 13")


def five_lists():
    sum_more_100 = []
    sum_less_100 = []
    for l in sum_lists:
        if l >= 100:
            sum_more_100.append(l)
        elif l < 100:
            sum_less_100.append(l)
        elif not sum_less_100 or not sum_more_100:
            print("No lists")
    print("sum_more_100:", sum_more_100)
    print("sum_less_100:", sum_less_100)


five_lists()

# 14 Написать функцию, которая получив на вход ваш возраст,
# выведет вам через какой срок вы сумеете отложить
# 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
print("task 14")

age = int(input("How old are you? age = "))


def investing(age):
    if age < 20:
        print("10 000$")
    if age < 30:
        print("20 000$")
    if age < 40:
        print("30 000$")
    if age < 50:
        print("50 000$")
    if age < 60:
        print("100 000$")
    if age > 60:
        print("more $")


investing(age)

#15 Написать функцию которая получив на вход стартовую ЗП Junior QA
# и количество лет стажа выведет в консоль прогресс роста
# ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список,
# полезных для компании, активностей которые может делать QA.
# Free implementation of function body logic

#16 Написать скрипт, который сгенерирует список имён пользователей.
# Список имён вывести в консоль.
names = ['Nadya', 'Katya', 'Viktor', 'Stas']
digits = []
rand = random.randint(0, 10)
for i in range(rand):

    d_int = random.randint(0, 10)
    digits.append(d_int)
    print('d_item', d_int)

print('digits_not_sorted =', digits)
digits.sort()
print('digits_sorted =', digits)

print('names_not_sorted =', names)
digits.sort()
print('names_sorted =', names)