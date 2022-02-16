'''
еализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
'''


class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def split_date(cls, dd_mm_yyyy):
        spl_date = []

        for i in dd_mm_yyyy.split():
            if i != '=':
                if i != '_':
                    spl_date.append(i)

        return int(spl_date[0]), int(spl_date[1]), int(spl_date[2])

    def __str__(self):
        return f' Дата {Data.split_date(self.dd_mm_yyyy)}'

    @staticmethod
    def correct(day, month, year):

        if 1 < day <= 28:
            if 1 <= month <= 12:
                if 20221 >= year >= 0:
                    return f'Верно'
                else:
                    return f'ERROR год'
            else:
                return f'ERROR месяц'
        else:
            return f'ERROR день'


some_date = Data('1  _ 1 _ 2000')
print(some_date)
print(Data.correct(22, 12, 2020))
print(some_date.split_date('23 _ 10 _ 2017'))

