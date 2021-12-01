# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import functools
import random

numbers = [str(random.randint(-100, 150)) for _ in range(20)]

with open('5.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(numbers))

with open('5.txt', 'r', encoding='utf-8') as f:
    ln = f.read().split()

print(functools.reduce(lambda a, b: int(a) + int(b), ln))
