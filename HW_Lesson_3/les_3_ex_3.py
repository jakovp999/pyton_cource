def my_func (arg_1,arg_2,arg_3):
    s_1 = arg_1 + arg_2
    s_2 = arg_1 + arg_3
    s_3 = arg_2 + arg_3
    max_sum = max(s_1, s_2, s_3)
    return  max_sum

arg_1 = int(input(f'Введите арг=1 '))
arg_2 = int(input('Введите арг_2'))
arg_3 = int(input('Введите арг_3'))

print(f'Максимальная сумма {my_func(arg_1, arg_2, arg_3)}')
