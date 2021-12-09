# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Garments(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expenditure(self):
        pass


class Coat(Garments):
    @property
    def expenditure(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Garments):
    @property
    def expenditure(self):
        return round(2 * self.param + 0.3, 2)


short_coat = Coat(48)
business_suit = Costume(1.7)

print(short_coat.expenditure)
print(business_suit.expenditure)
