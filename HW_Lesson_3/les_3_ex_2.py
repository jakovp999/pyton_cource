def my_dict(**kwargs):
    return kwargs

dict_user = my_dict(Имя='Ганс', фамилия = 'Вайсман', год_рождения = 1950, город_проживания = 'Париж', email = '123@345.com', телефон = '1234567893')
print(dict_user)

n = input('Ведите имя')
dict_user_1 = my_dict(имя = n )
print(dict_user_1)


