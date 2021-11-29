# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]

while True:
    print(my_list)
    number = input('Введите натуральное число или любой символ для остановки: ')
    if number.isdigit() and number != '0':
        number = int(number)
        if number == 1 or number < min(my_list):
            my_list.insert(len(my_list), number)
        elif number > max(my_list):
            my_list.insert(0, number)
        else:
            for ind, value in enumerate(my_list):
                if value < number:
                    my_list.insert(ind, number)
                    break
    else:
        break

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
