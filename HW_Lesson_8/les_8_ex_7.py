'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
'''


class Complex_numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self, ):
        return f'{self.x} + ({self.y} * i)'

    def __add__(self, other):
        return f' {self.x + other.x} + ({self.y + other.y}*i)'

    def __mul__(self, other):
        return f' {(self.x * other.x - self.y * other.y)} + ({(self.x * other.y + self.y * other.x)} *i)'


'''
произведением комплексных чисел
z_1 = a + bi и z_2 = c + di,
записанными а алгебраической форме, называется комплексное число
z_1 * z_2 = (ac - bd) + (ad + bc)i
'''

z_1 = Complex_numbers(2, -2)
print(f' z_1 = {z_1}')
z_2 = Complex_numbers(5, 7)
print(f' z_2 = {z_2}')

print(f' z_1 + z_2 = {z_1 + z_2}')
print(f' z_1 * z_2 = {z_1 * z_2}')
