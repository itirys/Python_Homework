# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial
from change import beautiful_numbers

def fact(n):
    for numb in n:
        yield numb, factorial(numb)


n = list(range(1, 11))

for el in fact(n):
    print(f'{el[0]}! = {" * ".join([str(num) for num in range(1, el[0]+1)])} = {beautiful_numbers(el[1])}')
