# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
import itertools, random

stop = 10

def iter_1(start):
    for number in itertools.count(start):
        if number > stop:
            break
        print(number)

iter_1(int(input('start: ')))


work_list = [random.randint(1, 10) for _ in range(3)]
print(work_list)

cycler = itertools.cycle(work_list)
for i in range(stop):
    print(next(cycler))
