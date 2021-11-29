"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
   і вертатиме список простих чисел всередині цього діапазона.
"""


def prime_list(num_start, num_finish):

    def is_prime(num):

        k = 0
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                k += 1
        if k <= 0:
            return True
        else:
            return False

    return [num for num in range(num_start, num_finish + 1) if is_prime(num)]


number_start = int(input("Ведіть число початок діапазону: "))
number_finish = int(input("Ведіть число кінець діапазону: "))

print(prime_list(number_start, number_finish))
