"""
8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник,
   з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
        Приклад виводу при введеному значенні 5 :
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


number = int(input('Please enter a number:'))
key_list = [i for i in range(number+1)]
value_list = []
for index in key_list:
    value = index * index
    value_list.append(value)
my_dict = dict(zip(key_list, value_list))
print(my_dict)
