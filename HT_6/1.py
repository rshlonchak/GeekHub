"""
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного,
   а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори.
   Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""


import time

GREEN_RED = 'Green    Red'
YELLOW_RED = 'Yellow   Red'
RED_GREEN = 'Red      Green'


def traffic_lights():
    timer = 0
    while True:
        if 0 <= timer < 4:
            print(GREEN_RED)
        elif 4 <= timer < 6:
            print(YELLOW_RED)
        elif 6 <= timer < 10:
            print(RED_GREEN)
        elif 10 <= timer < 12:
            print(YELLOW_RED)

        if timer >= 11:
            timer = 0
        else:
            timer += 1

        time.sleep(1)


traffic_lights()


