# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_user = int(input('Введите время в секундах: '))

hour_time = time_user // 3600
sec_time = time_user - 3600 * hour_time

min_time = sec_time // 60
sec_time = sec_time - min_time * 60

if hour_time < 10:
    hour_time = '0' + str(hour_time)

if min_time < 10:
    min_time = '0' + str(min_time)

if sec_time < 10:
    sec_time = '0' + str(sec_time)

print(f'{hour_time}:{min_time}:{sec_time}')