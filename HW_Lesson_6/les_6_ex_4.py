'''
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' Поехали {self.name}'

    def stop(self):
        return f' Стоим {self.name}'

    def turn_right(self):
        return f' Повернул на право {self.name}'

    def turn_left(self):
        return f'Повернул на лево {self.name}'

    def show_speed(self):
        return f' {self.name} скорость  {self.speed} км/ч'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' скорость {self.name} равна {self.speed} км/ч')
        if self.speed > 60:
            return f' скорость {self.name} выше нормы {self.speed} км/ч'
        else:
            return f' скорость {self.name} в норме {self.speed} км/ч'



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f' скорость {self.name} равна {self.speed} км/ч')
        if self.speed > 40:
            return f' скорость {self.name} выше нормы {self.speed} км/ч'
        else:
            return f' скорость {self.name} в норме {self.speed} км/ч'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


mers = Car(20, 'белый', 'Mersedes', False)
maz = WorkCar(50, 'черный', 'Маз', False)
bmw = SportCar(100, 'Синий', 'BMW', False)
lada = TownCar(80,'Зеленый', 'Lada', False)
print(mers.go())
print(mers.show_speed())
print(f' {maz.turn_left()}  {maz.show_speed()}')
print(f' {bmw.turn_right()} {bmw.show_speed()}')
print(f'{lada.go()}  {lada.show_speed()} в это же время {maz.stop()}')
