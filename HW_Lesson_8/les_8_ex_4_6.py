'''
Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные
типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
'''
'''
Продолжить работу над первым заданием. Разработайте методы, которые 
отвечают за приём оргтехники на склад и 
передачу в определённое подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру 
(например, словарь).
'''
'''
Продолжить работу над вторым заданием. Реализуйте механизм 
валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, 
нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте 
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

class Orgtechnik:
    __id = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__id = Orgtechnik.__id
        Orgtechnik.__id += 1

    def get_id(self):
        return self.__id


class Printer(Orgtechnik):
    def to_print(self):
        return f'Цвет {self.color} '


class Scanner(Orgtechnik):
    def to_scan(self):
        return f'Сканер штрихкода {self.size} '


class Copier(Orgtechnik):
    def to_copier(self):
        return f'Формат листа  {self.format_paper} '


class Seller:
    __id = 0

    def __init__(self, name):
        self.name = name
        self.orgtechniks = []
        Seller.__id += 1

    def get_id(self):
        return self.__id

    def add_orgtechnik(self, orgtechnik):
        self.orgtechniks.append(orgtechnik)

    def sell_technik(self, orgtechnik):
        if orgtechnik in self.orgtechniks:
            self.orgtechniks.remove(book)
            return True
        return False


class Shop:
    def __init__(self):
        self.curent_orgtechniks = {}

    def __str__(self):
        return f' {cu}'

    def add_orgtechnik(self, orgtechniks):
        for orgtechnik in orgtechniks:
            orgtechnik_id = orgtechnik.get_id()
            if self.curent_orgtechniks.get(orgtechnik_id):
                self.curent_orgtechniks[orgtechnik_id] += 1
            else:
                self.curent_orgtechniks[orgtechnik_id] = 1

    def remove_orgtechnik(self, orgtechnik):
        orgtechnik_id = orgtechnik.get_id()
        if self.curent_orgtechniks.get(orgtechnik_id):
            self.curent_orgtechniks[orgtechnik_id] -= 1
            if self.curent_orgtechniks[orgtechnik_id] == 0:
                self.curent_orgtechniks.pop(orgtechnik_id)
            return True
        else:
            return False

    def give_orgtechnik(self, orgtechnik, seller):
        if self.remove_orgtechnik(orgtechnik):
            seller.add_orgtechnik(orgtechnik)
        else:
            print(' в магазине нет такого товара ')


# оргтехника
my_orgtech_1 = Orgtechnik('hp', 2000, 1)
my_orgtech_2 = Orgtechnik('IBM', 1500, 1)
my_orgtech_3 = Orgtechnik('Canon', 1200, 5)

# добавление оргтехники в список
my_orgtechniks = [my_orgtech_1, my_orgtech_2, my_orgtech_3]
my_orgtechniks_1 = [my_orgtech_3, my_orgtech_2]
my_orgtechniks_2 = [my_orgtech_1, my_orgtech_2]

# добавление оргтехники в магазин
my_shop = Shop()
my_shop.add_orgtechnik(my_orgtechniks)
my_shop.add_orgtechnik(my_orgtechniks_1)
my_shop.add_orgtechnik(my_orgtechniks_2)

print(f' Техники в магазине {my_shop.curent_orgtechniks}')

my_seller = Seller('Jak')
print(f' Куплено {my_seller.orgtechniks}')

my_shop.give_orgtechnik(my_orgtech_1, my_seller)
print(f' Куплено give {my_seller.orgtechniks}')
print(f' Осталось {my_shop.curent_orgtechniks}')
