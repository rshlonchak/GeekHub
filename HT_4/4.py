"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
   і вертатиме список простих чисел всередині цього діапазона.
"""


def prime_list(num_start, num_finish):

    def is_prime(num):

        for divider in [2, 3, 5, 7]:
            if num != divider and not num % divider:
                return False
        return True

    return [num for num in range(num_start, num_finish + 1) if is_prime(num)]


number_start = int(input("Ведіть число початок діапазону: "))
number_finish = int(input("Ведіть число кінець діапазону: "))

print(prime_list(number_start, number_finish))
