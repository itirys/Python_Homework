# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

n, profit = 0, 0
firms = {}

with open('firms.txt', 'r', encoding='utf-8') as f:
    while True:
        firma = f.readline().split()
        if not firma:
            break
        else:
            n += 1
            firms[firma[0]] = int(firma[2]) - int(firma[3])
            profit += (int(firma[2]) - int(firma[3])) if (int(firma[2]) - int(firma[3])) > 0 else 0

with open('firms_profit.json', 'w') as f:
    f.write(json.dumps([firms, {'average_profit': round(profit / n)}]))

# with open('firms_profit.json', 'r') as f:
#     firms_j = json.load(f)
#
# print(firms_j)
