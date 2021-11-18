"""
6. Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False
"""


number_list = list(input('Please enter a list of objects:'))
number = input('Please enter a number:')
if number in number_list:
    print(True)
else:
    print(False)
