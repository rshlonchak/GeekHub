"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
   и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""


def is_prime(num):
    if 0 < num < 1000:
        if num != 2 and num % 2 == 0:
            return False
        elif num != 3 and num % 3 == 0:
            return False
        elif num != 5 and num % 5 == 0:
            return False
        elif num != 7 and num % 7 == 0:
            return False
        else:
            return True
    else:
        return "Число поза межами діапазону"


number = int(input("Ведіть число: "))

print(is_prime(number))
