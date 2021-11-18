"""
1 .Write a script which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
        Sample data : 1, 5, 7, 23
        Output :
        List : [‘1', ' 5', ' 7', ' 23']
        Tuple : (‘1', ' 5', ' 7', ' 23')
"""


number = input('Please enter a sequence of numbers separated by commas:')
number_list = list(number.split(','))
number_tuple = tuple(number.split(','))
print(number_list)
print(number_tuple)
