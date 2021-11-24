# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#   имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
options_fields = {'имя': '', 'фамилия': '', 'год рождения': '', 'город проживания': '', 'email': '', 'телефон': ''}

def query_options():
    """запрашивает данные пользователя"""
    i = 0
    for field in options_fields.keys():
        options_fields[field] = input(f'Введите параметр "{field}": ')
        i += 1
    return options_fields

def show_options(name, surname, year_birth, city, email, phone):
    """Выводит данные пользователя одной строкой"""
    print(f'{name} {surname}, {year_birth} г. р., проживает в г. {city}, e-mail: {email}, тел. {phone}')

def main():
    date_user = query_options()
    show_options(date_user['имя'], date_user['фамилия'], date_user['год рождения'], date_user['город проживания'], date_user['email'], date_user['телефон'])

main()