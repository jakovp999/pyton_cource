my_list = [7, 5, 3, 3, 2]
number_reiting = int (input('Введите число для определения рейтинга:   '))
len_my_list = len(my_list)
print(len_my_list)
for i in range(len_my_list):
    if number_reiting > my_list[i]:
        my_list.insert (i, number_reiting)
        reiting_n = i
        break
    elif number_reiting == my_list[i]:
        rate_n = (my_list.count(number_reiting))
        reiting_n = i + rate_n
        my_list.insert(reiting_n, number_reiting)
        break
    elif number_reiting < my_list[len_my_list-1]:
        my_list.insert(len_my_list, number_reiting)
        reiting_n = len_my_list
        break

print (f'Рейтинг числа {number_reiting} равен {reiting_n}')
print(my_list)

