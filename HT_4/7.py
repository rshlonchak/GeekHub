"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""


def double_counting(list_val):
    for i in set(list_val):
        if list_val.count(i) >= 1:
            print(i, '-', list_val.count(i))


my_list = [1, 1, 1, 2, 3, 3, 4, 4, 5, 6]

double_counting(my_list)
