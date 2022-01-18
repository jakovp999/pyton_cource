your_old = input('Введите ваш возраст :')
result_old = f'Ваш возраст {your_old} '
print(result_old)

your_name = input('Как вас завут?        ')
result_name = f'Привет {your_name} Как у вас дела?    '
print(result_name)
your_dela = input()

result_all = f'Привет {your_name}, тебе {your_old}, дела у тебя {your_dela}'
print(result_all)

before_old = int(input('лет назад:  '))
young_old = int(your_old) - before_old
result_young = f'Тебе было {young_old}'
print(result_young)
