# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from time import sleep
from random import choice


class Car:
    current_speed = 0
    is_police = False
    racing = 10

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def show_speed(self, current_speed):
        print(f'Текущая скорость {self.name}: {current_speed}')

    def go(self):
        print(f'машина {self.name} поехала')
        for self.current_speed in range(self.current_speed + self.racing, self.speed, self.racing):
            self.show_speed(self.current_speed)
            sleep(3)

    def stop(self):
        while self.current_speed != 0:
            self.current_speed -= 25
            if self.current_speed < 0:
                self.current_speed = 5
                break
            else:
                self.show_speed(self.current_speed)
                sleep(3)
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        while self.current_speed > 30:
            self.current_speed -= 30
            self.show_speed(self.current_speed)
            sleep(3)
        print(f'машина {self.name} повернула {direction}')


class TownCar(Car):
    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, name, speed, color, racing):
        Car.__init__(self, name, speed, color)
        self.racing = racing


class WorkCar(Car):
    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color)
        self.is_police = True

    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 60:
            print('Включен проблесковый маячок')
            if current_speed > 100:
                print('Включен звуковой сигнал')


vw = TownCar('Volkswagen', 180, 'белый')
zaz = TownCar('Запорожец', 80, 'голубой')
subaru = SportCar('Subaru BRZ', 226, 'серебристый', 35)
tractor = WorkCar('Трактор "Беларусь"', 35, 'Желтый')
gaz = PoliceCar('ГАЗ', 130, 'синий')

turn_direction = ['налево', 'направо']

for car in [zaz, vw, subaru, tractor, gaz]:
    print(f'{"-" * 30}\n{car.name}:\nцвет – {car.color}\nмаксимальная скорость – {car.speed} км/ч\n'
          f'Полицейская – {"да" if car.is_police == True else "нет"}')
    sleep(2)
    car.go()
    car.turn(choice(turn_direction))
    car.go()
    car.stop()
    sleep(2)
