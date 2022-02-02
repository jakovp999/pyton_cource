from functools import reduce

list_ish = [el for el in range(100, 1001) if el % 2 == 0]
print('Исходный список, четные от 100 до 1000 :', list_ish)

list_proizv = reduce(lambda x, y: x * y, list_ish)
print(type(list_proizv))
print('Результат :', list_proizv)
