# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_user = input('Введите число: ')

number_1 = int(number_user + number_user)
number_2 = int(number_user + number_user + number_user)

print(int(number_user) + number_1 + number_2)