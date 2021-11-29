"""
6. Вводиться число.
   Якщо це число додатне, знайти його квадрат,
   якщо від'ємне, збільшити його на 100,
   якщо дорівнює 0, не змінювати.
"""


def number_conversion(num):
    if num > 0:
        return num ** 2
    elif num < 0:
        return num + 100
    return num


number = int(input("Введіть число: "))

print(number_conversion(number))
