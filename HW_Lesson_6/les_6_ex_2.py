'''
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:
    # _length = 1
    # _width = 1

    def massa(self, _length, _width, _asfmas, _hight):
        self._width = _width
        self._length = _length
        self._asfmas = _asfmas
        self._hight = _hight
        return self._width * self._length * self._asfmas * self._hight


r = Road()
print(f' {r.massa(20, 10, 0.5, 5)} тонн')
print(f' ширина {r._length} м, длина {r._width} м, масса 1 кв метра, толщиной 1см {r._asfmas} т, толщина {r._hight} см')