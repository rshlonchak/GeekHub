"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""


class LoginException(Exception):
    pass


def check(username, password):
    list_digit = '0123456789'

    if len(username) < 3:
        raise LoginException('Username is too short, must be 3 or longer')
    elif len(username) > 50:
        raise LoginException('Username is too long, must be 50 or shorter')
    elif username[0] == '/':
        raise LoginException('There is not a command field')
    elif ' ' in username:
        raise LoginException('Username must not contain spaces')
    elif username == 'GOD':
        raise LoginException('This user is already exists')
    elif '\\' in username:
        raise LoginException('SQL is banned')
    elif len(password) < 8:
        raise LoginException('Password is too short, must be at least 8')
    elif len(set(password).intersection(list_digit)) == 0:
        raise LoginException('Password must contain digit')
    else:
        return True


user_name = input("name: ")
user_password = input("password: ")

print(check(user_name, user_password))
