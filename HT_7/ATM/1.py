"""
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.txt>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій
      (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число;
      знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається.
      Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль.
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
      (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
"""


import json
from datetime import datetime


def extract_users(filename):
    with open(filename) as f:
        lines = f.readlines()
        users = []
        for line in lines:
            username, password = line.strip().split('/')
            users.append(dict(name=username, password=password))
    return users


def verify_user(users, username, password):
    found_users = list(filter(lambda user: user['name'] == username and user['password'] == password, users))
    return False if not len(found_users) else True


def check_balance(username, password, users_filename='users.data'):
    users = extract_users(users_filename)
    if not verify_user(users, username, password):
        print("Invalid credentials")
        return

    with open(f'{username}_balance.data', 'r+') as f:
        lines = f.readlines()
        if not len(lines):
            f.writelines(str(0))

    with open(f'{username}_balance.data', 'r') as f:
        money = int(f.read())
        print(f'Баланс на вашому рахунку {money}')


def insert_money(username, password, amount, users_filename='users.data'):
    users = extract_users(users_filename)

    if not verify_user(users, username, password):
        print("Invalid credentials")
        return

    with open(f'{username}_balance.data', 'r+') as f:
        lines = f.readlines()
        if not len(lines):
            f.writelines(str(0))

    with open(f'{username}_balance.data', 'r') as f:
        lines = int(f.readlines()[0])

    with open(f'{username}_balance.data', 'w+') as f:
        f.writelines(str(lines + amount))

    print(f"Рахунок поповнено на {amount}")

    with open(f'{username}_transactions.data', 'r+') as f:
        try:
            list_json = json.load(f)
        except json.decoder.JSONDecodeError:
            list_json = []
        f.seek(0)
        f.truncate()
        list_json.append(f"Balance replenished on {amount} at {datetime.now()}")
        json.dump(list_json, f)


def withdraw_money(username, password, amount, users_filename='users.data'):
    users = extract_users(users_filename)

    if not verify_user(users, username, password):
        print("Invalid credentials")
        return

    with open(f'{username}_balance.data', 'r+') as f:
        lines = f.readlines()
        if not len(lines):
            f.writelines(str(0))

    with open(f'{username}_balance.data', 'r') as f:
        balance = int(f.readlines()[0])
        if amount > balance:
            print(f"Недостатньо коштів\nВаш баланс {balance}\nВведена сума перевищує залишок на рахунку")
        else:
            with open(f'{username}_balance.data', 'w') as fl:
                fl.writelines(str(balance - amount))

            with open(f'{username}_transactions.data', 'r+') as file:
                try:
                    list_json = json.load(file)
                except json.decoder.JSONDecodeError:
                    list_json = []
                file.seek(0)
                file.truncate()
                list_json.append(f"Removed from the balance {amount} at {datetime.now()}")
                json.dump(list_json, file)


def start(users_filename='users.data'):
    while True:
        username = input("Введіть ім'я: ")
        password = input("Введіть пароль: ")

        users = extract_users(users_filename)

        if not verify_user(users, username, password):
            print("Такого користувача не знайдено")
            continue

        print('''            1 - Продивитись баланс
            2 - Поповнити баланс
            3 - Зняти кошти
            4 - Вихід''')

        number = int(input("Введіть число: "))

        if number == 1:
            check_balance(username, password)
        elif number == 2:
            amount = int(input("Введіть суму: "))
            insert_money(username, password, amount)
        elif number == 3:
            amount = int(input("Введіть суму: "))
            withdraw_money(username, password, amount)
        elif number == 4:
            print("Дякуємо що скористались послугами банку")
            return
        else:
            print("Неправильна команда для проведення операції")
            continue


if __name__ == '__main__':
    start()
