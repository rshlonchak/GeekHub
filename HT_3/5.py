"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y"
і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює y
"""


def difference():
    input_x = int(input("Введіть перше число: "))
    input_y = int(input("Введіть перше число: "))
    if input_x > input_y:
        z = input_x - input_y
        return str(input_x) + " більше нiж " + str(input_y) + " на " + str(z)
    elif input_x < input_y:
        z = input_y - input_x
        return str(input_y) + " більше нiж " + str(input_x) + " на " + str(z)
    elif input_x == input_y:
        return str(input_x) + " дорівнює " + str(input_y)


print(difference())
