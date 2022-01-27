def my_func (arg_1, arg_2):
    stepen = 1
    for i in range (arg_2):
        stepen = stepen * arg_1
    result_step = 1/stepen
    return result_step


arg_1 = int(input(f'Введите арг=1 '))
arg_2 = int(input('Введите арг_2'))

print(f'{arg_1} в степени -{arg_2} равно {my_func(arg_1, arg_2)}')
