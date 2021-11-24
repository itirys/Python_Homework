# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_user = []
element = ''

while True:
    element = input('Введите элемент списка или "stop" для остановки: ')
    if element == 'stop':
        break
    list_user.append(element)

i = 0
count = len(list_user) if len(list_user) % 2 == 0 else len(list_user) - 1

while i < count:
    var_1, var_2 = list_user[i], list_user[i+1]
    list_user[i], list_user[i+1] = var_2, var_1
    i += 2

print(list_user)



