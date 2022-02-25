'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes_all(ABC):

    @abstractmethod
    def square_coat(self):
        pass

    @abstractmethod
    def square_suit(self):
        pass

    @abstractmethod
    def square_all(self):
        pass


class Clothes(Clothes_all):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def square_coat(self):
        return (f'Ткани на пальто \n'
                f'{(self.size / 6.5 + 0.5)}')

    @property
    def square_suit(self):
        return (f'Ткани на костюм \n'
                f'{(2 * self.height + 0.3)}')

    @property
    def square_all(self):
        return str(f'Всего ткани \n'
                   f'{(self.size / 6.5 + 0.5 + 2 * self.height + 0.3)}')


class Dress(Clothes_all):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def square_coat(self):
        return (f'Ткани на платье \n'
                f'{(self.size / 6.0 + 0.7)}')

    # @property
    def square_suit(self):
        pass

    def square_all(self):
        pass


coat = Clothes(5, 2)
print(coat.square_coat)
print(coat.square_suit)
print(coat.square_all)

dress = Dress(4, 7)
print(dress.square_coat)
