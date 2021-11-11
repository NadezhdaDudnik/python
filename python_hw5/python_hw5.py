import random
from random import randint
import numpy as np

# 1. Написать скрипт который в создаст список целых чисел.
list_generator = list(range(70));
print("list_generator", list_generator);


def full_random(list_length):
    core_items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in range(list_length):
        result.append(random.choice(core_items))
    return print("numbers", result)


full_random(70)

# 2 Написать скрипт который в создаст список целых чётных чисел.
list_generator_even = list(range(0, 70, 2));
print("list_generator_even", list_generator_even);

# 3 Написать скрипт который в создаст список целых нечётных чисел.
list_generator_odd = list(range(1, 70, 2));
print("list_generator_odd", list_generator_odd);

# 4 Написать скрипт который из списка целых чисел выведет чётные числа.
even_list = [];
lists = list(range(70));
for i in lists:
    if i % 2 == 0:
        # print("i", i);
        even_list.append(i);
print("even_list =", even_list);

# 5 Написать скрипт который из списка целых чисел выведет нечётные числа.
odd_list = [];
lists = list(range(70));
for i in lists:
    if i % 2 != 0:
        # print("i", i);
        odd_list.append(i);
print("odd_list =", odd_list);

# 6 Написать скрипт который из списка целых чисел выведет чётные числа
# которые делятся на 5 без остатка.
five_list = [];
lists = list(range(70));
for i in lists:
    if i % 2 == 0 and i % 5 == 0:
        five_list.append(i);
print("five_list = ", five_list);

# 7 Написать скрипт который из списка целых чисел выведет количество
# чётных чисел которые делятся на 5 без остатка.
count_five_list = [];
lists = list(range(0, 70));
for i in lists:
    if i % 2 == 0 and i % 5 == 0:
        count_five_list.append(i);
print("count_five_list", len(count_five_list));

# 8 Написать скрипт который в создаст список целых рандомных чисел.
# [ выражение for переменная in список]
generator = [randint(1, 70) for i in range(70)];
print("random_generator =", generator);


# 9 Написать функцию которая, получив на вход любой из выше
# созданных списков, разобьёт его списки по 5 элементов.
def lists_split():
    lists1 = list(range(70));
    split_list = np.array_split(lists1, 14)
    return print("split_list =", split_list)


lists_split()


# 10 Написать функцию которая, получив на вход список целых чисел,
# вернёт 2 списка, список чётных и список нечётных чисел.

# Нарезка последовательностей поддерживает не только указание
# начального и конечного значения, но и шага (или шага);
# [::2] выбирает каждое второе значение, начиная с 0,
# [1::2] -каждое значение, начиная с 1.

def lists_split_odd_even():
    lists2 = list(range(70));
    even, odd = lists2[::2], lists2[1::2]
    return print("even list =", even, "odd list =", odd)


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


split_even_odd(lists)
print("+++++++++++++++++++++++++++=")
# 11 Написать скрипт который сгенерирует список под названием 5_stars
# из списков по 5 элементов целых чисел.
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_3 = [11, 12, 13, 14, 15]
five_stars = list_1, list_2, list_3
print("five_stars =", five_stars)

# 12 Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
# При этом используется комбинация zip и * для распаковки списка,
# а затем архивирование элементов в соответствии с их индексом.
# Затем вы используете понимание списка,
# чтобы перебрать группы похожих индексов, суммируя их и возвращаясь в их «исходную» позицию.

sum_lists = [sum(k) for k in zip(*five_stars)]
print("sum lists =", sum_lists)


def foo():
    # initialise length of data(n) and sum_of_col variable
    n = len(five_stars)
    print(n)
    sum_of_col = []
    # iterate over column
    for col_i in range(n):
        # column sum
        col_count = 0;
        # iterate over row
        for row_i in range(n):
            col_count += five_stars[row_i][col_i]
        # append sum of column to list
        sum_of_col.append(col_count)
    return print("sum_of_col =", sum_of_col)


foo()

# 13 Написать функцию которая на вход получает список 5_stars,
# а вернёт 2 списка. В одном списке внутренние списки из 5_stars
# сумма чисел которых >= 100, а другой сумма чисел которых < 100.
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”

# 14 Написать функцию которая получив на вход ваш возраст,
# выведет вам через какой срок вы сумеете отложить
# 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.


#15 Написать функцию которая получив на вход стартовую
# ЗП Junior QA и количество лет стажа выведет в консоль п
# рогресс роста ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список,
# полезных для компании, активностей которые может делать QA.
# Free implementation of function body logic