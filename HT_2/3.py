"""
3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""


first_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), 'd', '', []]
last_list = []
for i in first_list:
    if len(i) > 0:
        last_list.append(i)

print(last_list)
