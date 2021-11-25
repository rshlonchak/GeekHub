"""
7. Ну і традиційно -> калькулятор :)
   повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


print("0 при введенні замість знаку завершить функцію")
while True:
    operation = input("Введіть знак (+,-,*,/): ")
    if operation == '0':
        break
    if operation in ('+', '-', '*', '/'):
        first_value = float(input("Перше значення= "))
        second_value = float(input("Друге значення= "))
        if operation == '+':
            print(first_value + second_value)
        elif operation == '-':
            print(first_value - second_value)
        elif operation == '*':
            print(first_value * second_value)
        elif operation == '/':
            if second_value != 0:
                print(first_value / second_value)
            else:
                print("Ділення на 0!")
    else:
        print("неправильний знак")
