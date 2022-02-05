import random

with open('rand_num_5.txt', 'w') as file:
    for _ in range(25):
        file.write(f'{random.randint(0, 30)} ')

with open('rand_num_5.txt', 'r') as file:
    str_chisel = file.read().split()
    print('Считаная строка', str_chisel)
    a = list(map(int, str_chisel))
    print('Преобразованная в INT строка', a)

    sum_chisel = sum(a)
    print('Сумма чисед', sum_chisel)
