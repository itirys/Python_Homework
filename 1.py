# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
def write_file(name, text, coding='utf-8'):
    """Запись строки в файл """
    with open(name, 'a', encoding=coding) as f:
        print('Записано!') if f.write(text) else print('Что-то пошло не так!')


while True:
    text = input('Введите строку для записи в файл или нажмите Enter для выхода: ')
    if len(text) > 0:
        write_file('1.txt', text + '\n')
    else:
        print('До скорой встречи!')
        break
