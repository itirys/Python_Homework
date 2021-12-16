# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.
class MyError(Exception):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def check(b):
        try:
            if b == 0:
                raise MyError('Ошибка! Деление на ноль!')
            return True
        except MyError as err:
            print(err)


def division(a, b):
    return round(a / b, 2)


def main():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if MyError.check(b):
        print(division(a, b))


main()
