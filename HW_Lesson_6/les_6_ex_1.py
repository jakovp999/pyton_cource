'''

Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import time


class TrafficLight:
    __color = ''

    def running(self):
        for i in range(2):
            __color = 'red'
            print('переключаемся')
            print(__color)
            time.sleep(7)

            __color = 'yellow'
            print('переключаемся')
            print(__color)
            time.sleep(2)

            __color = 'green'
            print('переключаемся')
            print(__color)
            time.sleep(5)

        print('Конец1111')


r = TrafficLight()
r.running()