# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('pers_salary.txt', 'r', encoding='utf-8') as f:
    ln = f.readlines()

pers_salary = {}
for i in range(len(ln)):
    var = ln[i].split(' -- ')
    pers_salary[var[0]] = int(var[1])

print(f'Сотрудники с окладом менее 20 тыс.: {[key for key in pers_salary.keys() if pers_salary[key] < 20000]}')

print(f'Средняя величина дохода сотрудников: {round(sum(pers_salary.values()) / len(ln), 2)}')
