# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:

    @classmethod
    def convert_data(cls, a):
        day, month, year = map(int, a.split('-'))
        return [day, month, year]

    @staticmethod
    def valid_date(a):
        date = Date.convert_data(a)
        day, month, year = date[0], date[1], date[2]
        if year > 1900:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 0 < day <= 31
            elif month in [4, 6, 9, 11]:
                return 0 < day <= 30
            elif month == 2:
                if (year % 4) == 0:
                    return 0 < day <= 29
                else:
                    return 0 < day <= 28
            else:
                return False
        else:
            return False


print(Date.valid_date('10-12-2021'))
print(Date.valid_date('10-12-21'))
print(Date.valid_date('10-13-2021'))
print(Date.valid_date('29-02-2021'))
print(Date.valid_date('28-02-2021'))
