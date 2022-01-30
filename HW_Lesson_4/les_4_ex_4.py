from collections import Counter

list_ish = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список', list_ish)

list_new_1 = [el for el in list_ish if list_ish.count(el) == 1]
print('Убраны повторяющиеся элементы списка', list_new_1)

print('Второй способ')
list_new = [el for el, i in Counter(list_ish).items() if i == 1]
print('Убраны повторяющиеся элементы списка', list_new)
