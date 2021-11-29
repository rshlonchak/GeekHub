"""
5. Написати функцію < fibonacci >, яка приймає один аргумент
   і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(num):
    num_fib_1 = 0
    num_fib_2 = 1
    print(num_fib_1, num_fib_2, end=' ')
    while num >= num_fib_2:
        print(num_fib_2, end=' ')
        num_fib_1, num_fib_2 = num_fib_2, num_fib_1 + num_fib_2
    return ''


number = int(input('Введіть число: '))
print(fibonacci(number))

