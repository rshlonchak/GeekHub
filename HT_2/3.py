"""
3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""


first_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), 'd', '', []]
last_list = []
for item in first_list:
    if len(item) > 0:
        last_list.append(item)

print(last_list)
