"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
   и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""


def is_prime(num):

    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False


number = int(input("Ведіть число: "))

print(is_prime(number))
