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


def traffic_lights():
    while True:
        green, red = 1, 1
        yellow_green, yellow_red = 1, 1
        while green < 5:
            print('{0:10}  {1}'.format('Green', 'Red'))
            green += 1
            time.sleep(1)
            while green > 4:
                print('{0:10}  {1}'.format('Yellow', 'Red'))
                yellow_green += 1
                time.sleep(1)
                while yellow_green > 3:
                    print('{0:10}  {1}'.format('Red', 'Green'))
                    yellow_red += 1
                    time.sleep(1)
                    while yellow_red > 3:
                        print('{0:10}  {1}'.format('Yellow', 'Green'))
                        red += 1
                        time.sleep(1)
                        if red > 3:
                            green, red = 1, 1
                            yellow_green, yellow_red = 1, 1


traffic_lights()


