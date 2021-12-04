# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом толщиной в 1 см * см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    mass = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        outlay = self._length * self._width * self.mass * self.thickness / 1000
        print(f'{self._length} м * {self._width} м * {self.mass} кг * {self.thickness} см = {outlay} т')


str_sesame = Road(5000, 20)
str_sesame.calc()
