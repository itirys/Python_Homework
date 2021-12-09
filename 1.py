# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# Результатом сложения должна быть новая матрица.
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        count_col = len(self.matrix[0])
        n = 0
        for i in range(count_col):
            for j in range(len(self.matrix)):
                n = len(str(self.matrix[j][i])) if n < len(str(self.matrix[j][i])) else n
        m = '{:' + str(n) + 'd}'
        for i in range(len(self.matrix)):
            str_matrix += '\t'.join(map(lambda el: m.format(el), self.matrix[i])) + '\n'
        return str_matrix

    def __add__(self, other):
        new_matrix = copy.deepcopy(self.matrix)
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(new_matrix)
        else:
            return 'Матрицы разной размерности!'


m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m2 = Matrix([[31, 22, 37], [32, 1000, -10], [43, 51, 86]])
print(m1, '\n')
print(m2, '\n')
print(m1 + m2)
