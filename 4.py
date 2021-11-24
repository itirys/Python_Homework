# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# 1-й вариант решения _______________________________

number_user = int(input('Введите целое положительное число: '))

i = 0
max_number = 0

while i < len(str(number_user)):
    if max_number < int(str(number_user)[i]):
        max_number = int(str(number_user)[i])
    i += 1

print(f'Самая большая цифра в числе: {max_number}\n')


# 2-й вариант решения _______________________________

number_user = int(input('Введите целое положительное число: '))

i = 0
numbers = []

while i < len(str(number_user)):
    numbers.append(int(str(number_user)[i]))
    i += 1

print(f'Самая большая цифра в числе: {max(numbers)}')