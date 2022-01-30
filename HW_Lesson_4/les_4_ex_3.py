# my_list = [i for i in range(20, 241)]
# print('Последовательность чисел от 20 до 240 ', my_list)
#
# new_list = [el for el in my_list if el % 20 == 0 or el % 21 == 0]
# print('Числа из заданной последовательности кратные 20 или 21', new_list)

# Более рашиональное решение
new_list_1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print('Числа из последовательности чисел от 20 до 240 кратные 20 или 21', new_list_1)
