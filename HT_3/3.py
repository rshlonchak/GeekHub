"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
   яка буде повертати пору року, якiй цей мiсяць належить
   (зима, весна, лiто або осiнь)
"""


def season(month):
    if month in range(1, 13):
        if 2 < month < 6:
            return "Весна"
        elif 5 < month < 9:
            return "Літо"
        elif 8 < month < 12:
            return "Осінь"
        else:
            return "Зима"
    else:
        return "Не існує такого місяця"


print(season(1))
print(season(3))
print(season(6))
print(season(9))
print(season(13))
