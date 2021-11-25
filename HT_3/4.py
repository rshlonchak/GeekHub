"""
4. Створiть 3 рiзних функцiї (на ваш вибiр).
   Кожна з цих функцiй повинна повертати якийсь результат.
   Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
   обробляє повернутий ними результат та також повертає результат.
   Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""


def this_multiplication(x, y):
    m = x * y
    return m


def this_difference(x, y):
    if x > y:
        dif = x - y
    else:
        dif = y - x
    return dif


def this_division(x, y):
    if x > y:
        div = x // y
    else:
        div = y // x
    return div


def this_sum():
    res = this_multiplication(2, 3) + this_difference(5, 7) + this_division(2, 7)
    return res


print(this_sum())
