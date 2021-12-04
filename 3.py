# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход: {total_income}\nВ том числе: оклад – {self._income["wage"]}; премия – {self._income["bonus"]}')


pers1 = Position('Василий', 'Иванов', 'менеджер', 50000, 50000)
pers2 = Position('Мария', 'Белкина', 'офис-менеджер', 25000, 25000)

for pers in [pers1, pers2]:
    pers.get_full_name()
    print(f'Должность: {pers.position}')
    pers.get_total_income()
    print('-' * 30)