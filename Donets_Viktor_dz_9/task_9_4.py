# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name,
# is_police(булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на{direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} привышает скорость!!!')
        print(f'Текущая скорость {self.name} = {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} привышает скорость!!!')
        print(f'Текущая скорость {self.name} = {self.speed}')


class PoliceCar(Car):
    pass


town_car = TownCar(90, 'Зеленая', 'Honda', False)
sport_car = SportCar(285, 'Черная', 'Maserati', False)
work_car = WorkCar(41, 'Белая', 'Renault', False)
police_car = PoliceCar(120, 'Синяя', 'Hyundai', True)

town_car.show_speed()
town_car.go()
town_car.turn('лево')
town_car.stop()
sport_car.show_speed()
sport_car.turn('право')
work_car.show_speed()
police_car.show_speed()
