def my_func(*args):
    if '!' in args[0]:
        arg_3 = list(args[0].split())
        print("преобразование to list при '!' : ", arg_3)
        simv_index = arg_3.index('!')
        print("индекс символа '!' :", simv_index)
        arg_4 = arg_3[0:simv_index]
        print("ряд до символа '!':", arg_4)
        arg_5 = list(map(int, arg_4))
        print("список integers : ", arg_5)
        arg_5_sum = sum(arg_5)
        print("Сумма ряда : ", arg_5_sum)
        num_list.append(arg_5_sum)
        print("Общий список cумм каждого ввода:  ", num_list)
        sum_all = sum(num_list)
        print("сумма общая: ", sum_all)
    else:
        print(f'список после ввода {args}')
        print(type(args))
        arg_1 = list(args[0].split())
        print("преобразование to list : ", arg_1)
        arg_2 = list(map(int, arg_1))
        print("список integers : ", arg_2)
        arg_2_sum = sum(arg_2)
        print("Сумма ряда : ", arg_2_sum)
        num_list.append(arg_2_sum)
        print("Общий список cумм каждого ввода:  ", num_list)
        sum_all = sum(num_list)
        print("сумма общая: ", sum_all)
    return sum_all

i = True
arg = []
num_list = []
while True:
    args = (input(f'Введите ряд   '))
    result = my_func(args)
    print("!!!!Oкончательный результат :", result)
    if '!' in args:
        break
    # if '!' in arg:
    #     arg_3 = list(arg.split())
    #     print("преобразование to list при '!' : ", arg_3)
    #     simv_index = arg_3.index('!')
    #     print("индекс символа '!' :",simv_index)
    #     arg_4 = arg_3[0:simv_index]
    #     print("ряд до символа '!':", arg_4)
    #     arg_5 = list(map(int, arg_4))
    #     print("список integers : ", arg_5)
    #     arg_5_sum = sum(arg_5)
    #     print("Сумма ряда : ", arg_5_sum)
    #     num_list.append(arg_5_sum)
    #     print("Общий список cумм каждого ввода:  ", num_list)
    #     sum_all = sum(num_list)
    #     print("сумма общая: ", sum_all)
    #     break
    # else:
    #     print(f'список после ввода {arg}')
    #     print(type(arg))
    #     arg_1 = list(arg.split())
    #     print("преобразование to list : ", arg_1)
    #     arg_2 = list(map(int, arg_1))
    #     print("список integers : ", arg_2)
    #     arg_2_sum = sum(arg_2)
    #     print("Сумма ряда : ", arg_2_sum)
    #     num_list.append(arg_2_sum)
    #     print("Общий список cумм каждого ввода:  ", num_list)
    #     sum_all = sum(num_list)
    #     print("сумма общая: ", sum_all)
else:
    somecode
