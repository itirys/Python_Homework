class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        """Объединение двух клеток: число ячеек общей клетки равняется сумме ячеек исходных двух клеток."""
        return self.count_cell + other.count_cell

    def __sub__(self, other):
        """Участвуют две клетки.
        Операция выполняется только если разность количества ячеек двух клеток больше нуля,
        иначе выводится соответствующее сообщение"""
        res = abs(self.count_cell - other.count_cell)
        return res if res > 0 else 'Разность количества ячеек двух клеток <= 0'

    def __mul__(self, other):
        """Создается общая клетка из двух: число ячеек общей клетки определяется
        как произведение количества ячеек этих двух клеток"""
        return self.count_cell * other.count_cell

    def __truediv__(self, other):
        """Создается общая клетка из двух: число ячеек общей клетки определяется
        как обычное (не целочисленное) деление количества ячеек этих двух клеток
        и осуществляется округление значения до целого числа"""
        return round(self.count_cell / other.count_cell) if self.count_cell > other.count_cell \
            else round(other.count_cell / self.count_cell)

    def make_order(self, row):
        """Организовывает ячейки по рядам. Принимает экземпляр класса и количество ячеек в ряду.
        Возвращает строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
        Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся"""
        res = self.count_cell // row
        rest = self.count_cell % row
        return (('*' * row + '\\n') * res + '*' * rest).strip('\\n')


a = Cell(12)
b = Cell(15)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
print(b.make_order(5))
