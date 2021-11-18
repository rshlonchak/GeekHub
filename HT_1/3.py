"""
3. Write a script to sum of the first n positive integers.
"""


n = int(input('Please enter a number:'))
s = 0
for i in range(0, n+1):
    s = s + i
print(s)
