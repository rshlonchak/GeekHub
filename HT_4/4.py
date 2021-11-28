"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
   і вертатиме список простих чисел всередині цього діапазона.
"""


def prime_list(num_start, num_finish):
    if num_finish > num_start:
        list_prime = []
        for i in range(num_start, num_finish + 1):
            if i != 2 and i % 2 == 0:
                continue
            elif i != 3 and i % 3 == 0:
                continue
            elif i != 5 and i % 5 == 0:
                continue
            elif i != 7 and i % 7 == 0:
                continue
            else:
                list_prime.append(i)
    else:
        return "Початкове значення не може бути більше чим кінцеве"
    return list_prime


number_start = int(input("Ведіть число початок діапазону: "))
number_finish = int(input("Ведіть число кінець діапазону: "))

print(prime_list(number_start, number_finish))
