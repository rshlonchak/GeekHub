"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
   і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
       інакше (<silent> == <False>) - породжується виключення LoginException
"""


class LoginException(Exception):
    pass


def auth(username, password, silent=False):
    list_user = [('Andrew', 'qwerty123'), ('Maxim', '1111'), ('Roma', 'awdrg_1357'),
                 ('Katya', 'cyvub'), ('Masha', 'yfubjbu')]

    for user, passw in list_user:
        if username == user and password == passw:
            return True

    if silent:
        return False
    raise LoginException("incorrect login or password")


user_name = input("name: ")
user_password = input("password: ")

print(auth(user_name, user_password, True))
print(auth(user_name, user_password))
