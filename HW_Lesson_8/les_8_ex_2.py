'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class Div_zero:
    def __init__(self, delim, delit):
        self.delim = delim
        self.delit = delit

    def exep_div_zero(self):
        try:
            return self.delim / self.delit
        except:
            return f' ERROR Деление на 0'


my_div_zero = Div_zero(20, 2)
print(my_div_zero.exep_div_zero())

my_div_zero = Div_zero(20, 0)
print(my_div_zero.exep_div_zero())
