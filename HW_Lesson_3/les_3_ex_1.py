def  my_div (arg_1, arg_2):
    """Деленин двух чисел
    В случае деленмя на 0
    выдает результат None
    """
    if arg_2 != 0:
        result = arg_1 / arg_2
        # result_div0 = None
    else:
        result = None

    return result

for i in range(3,0,-1):
    arg_1 = int(input(f'Введите арг=1 '))
    arg_2 = int(input('Введите арг_2'))
    num_div = my_div(arg_1, arg_2)
    if num_div != None:
        print(f' результат деленя {num_div}')
        break
    else:
        if i-1 != 0:
            print(f'У вас осталось {i-1} попыток')
        else:
            print('жаль, так и не получилось')
