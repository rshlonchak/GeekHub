"""
4. Write a script to concatenate N strings.
"""


number = int(input('Please enter a number:'))
sum_str = ""
for i in range(number):
    my_str = input('Please enter your strings:')
    sum_str += my_str
print(sum_str)
