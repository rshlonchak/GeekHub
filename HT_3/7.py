"""
7. Ну і традиційно -> калькулятор :)
   повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


def calculator(d, x, y):
    if d in ('+', '-', '*', '/'):
        if d == '+':
            print(x + y)
        elif d == '-':
            print(x - y)
        elif d == '*':
            print(x * y)
        elif d == '/':
            if y != 0:
                print(x / y)
            else:
                print("Ділення на 0!")


operation = input("Введіть знак (+,-,*,/): ")
first_value = float(input("Перше число= "))
second_value = float(input("Друге число= "))

calculator(operation, first_value, second_value)
