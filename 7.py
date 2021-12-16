class ComplexNumbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'z = {self.a}+{self.b}i' if self.b >= 0 else f'z = {self.a}{self.b}i'

    def __add__(self, other):
        k = "+" if (self.b + other.b) >= 0 else ""
        return f'z = ({self.a}{"+" if self.b >= 0 else ""}{self.b}i) + ' \
               f'({other.a}{"+" if other.b >= 0 else ""}{other.b}i) = ' \
               f'{self.a + other.a}{k}{self.b + other.b}i'

    def __mul__(self, other):
        k = "+" if (self.a * other.b + self.b * other.a) >= 0 else ""
        return f'z = ({self.a}{"+" if self.b >= 0 else ""}{self.b}i) * ' \
               f'({other.a}{"+" if other.b >= 0 else ""}{other.b}i) = ' \
               f'{self.a * other.a + (-1) * self.b * other.b}{k}{self.a * other.b + self.b * other.a}i'


z1 = ComplexNumbers(1, 3)
z2 = ComplexNumbers(4, -5)
z3 = ComplexNumbers(-3, 6)

print(z1)
print(z2)
print(z3)
print('*' * 40)
print(z1 + z2)
print(z1 + z3)
print(z2 + z3)
print('*' * 40)
print(z1 * z2)
print(z1 * z3)
print(z2 * z3)
