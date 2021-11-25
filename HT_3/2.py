"""
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл,
   який виведе всі високосні роки в цьому проміжку (границі включно).
"""

initial_year = int(input("Input initial year: "))
final_year = int(input("Input final year: "))

for year in range(initial_year, final_year+1):
    if year % 4 == 0 and year % 100 != 0:
        print(year)
    elif year % 400 == 0:
        print(year)
