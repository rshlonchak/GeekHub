"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
   и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""


def is_prime(num):
    if num > 1000:
        return "Число поза межами діапазону"
    for divider in [2, 3, 5, 7]:
        if num != divider and not num % divider:
            return False
    return True


number = int(input("Ведіть число: "))

print(is_prime(number))
