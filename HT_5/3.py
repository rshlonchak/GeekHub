"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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
        raise LoginException('Password must not contain spaces')
    elif username == 'GOD':
        raise LoginException('This user is already exists')
    elif len(password) < 8:
        raise LoginException('Password is too short, must be at least 8')
    elif len(set(password).intersection(list_digit)) == 0:
        raise LoginException('Password must contain digit')
    else:
        return True


def validate(username, passw):
    try:
        check(username, passw)
        return 'OK'
    except LoginException as error:
        return error


list_user = [('Andrew', 'qwerty123'), ('Maxim', '1111'), ('Artem Ivanov', 'awdrg_1357'),
             ('K', 'cyaefvub'), ('Masha', 'yfubrjbu'), ('/sudo rm -rf', '12345678')]

for name, password in list_user:
    print(f'Name: {name}\nPassword: {password}\nStatus: {validate(name, password)}', end='\n\n')
