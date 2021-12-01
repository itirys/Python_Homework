# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def expo_write(ln):
    str_list = ln.split(' — ')
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(f'{numerals[str_list[0]]} — {int(str_list[1])}\n')


def expositor(name='text.txt'):
    i, n = -1, 0
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            ln = f.readline()
            i += 1
            if not ln:
                print(f'Прочитано: {i} строк(и)\nЗаписано в text1.txt: {n} строк(и)')
                break
            else:
                expo_write(ln)
                n += 1


expositor()
