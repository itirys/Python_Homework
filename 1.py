# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def query_numbs():
    """Запрашивает у пользователя два числа"""
    numbs = []
    i = 0
    while i < 2:
        numb = input(f'Введите {i+1}-е число: ')
        if numb.isdigit():
            numbs.append(int(numb))
            i += 1
        else:
            print('Ошибка! Необходимо ввести число!')
    return numbs

def division(numbs):
    """Делит одно число на другое число"""
    if numbs[1] == 0:
        print('Ошибка! Делить на 0 нельзя!')
        return False
    else:
        return round(numbs[0] / numbs[1], 2)

def main():
    while True:
        numbs = query_numbs()
        if division(numbs):
            print(f'{numbs[0]} / {numbs[1]} = {division(numbs)}')
            break

main()