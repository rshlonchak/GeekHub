"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
   -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя - > (видаляє перші 50 символів і прінтує все інше)
"""


def difference(input_str):
    if 29 < len(input_str) < 51:
        print(len(input_str))

    elif len(input_str) < 30:
        input_str_num = "".join(filter(str.isdigit, input_str))
        sum_num = 0
        for item in list(input_str_num):
            sum_num = sum_num + int(item)
        print(sum_num)
        print("".join(filter(str.isalpha, input_str)))
    else:
        print(input_str[50:])


input_string = input("Введіть ваш рядок: ")

difference(input_string)
