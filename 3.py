# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
user_month = 0
while user_month > 12 or user_month < 1:
    user_month = input('Введите порядковый номер месяца: ')
    user_month = int(user_month) if user_month.isdigit() else 0
    if user_month > 12 or user_month < 1:
        print('Месяцы считаются от 1 до 12!')

# Решение через list
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

i = 0

while i < 4:
    if user_month in month[i]:
        print(seasons[i])
    i += 1

# Решение через dict
month_seasons = {
    12: 'Зима', 1: 'Зима', 2: 'Зима',
    3: 'Весна', 4: 'Весна', 5: 'Весна',
    6: 'Лето', 7: 'Лето', 8: 'Лето',
    9: 'Осень', 10: 'Осень', 11: 'Осень'
}

print(month_seasons[user_month])
