# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'\n{self.title}. Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('123' * 10)


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('*' * 30)


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('=-=' * 10)


pero = Pen('Перьевая ручка')
pero.draw()

pencil_black = Pencil('Черный карандаш')
pencil_black.draw()

handle1 = Handle('Маркер № 1')
handle1.draw()
