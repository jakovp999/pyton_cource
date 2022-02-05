viruchka = int(input('Введите выручку предприятия:  '))
zatraty = int(input('Введите затраты предприятия:   '))
kolv_sotr = int(input('Введите колличество сотрудников:   '))

if viruchka > zatraty:
    result = viruchka - zatraty
    print(f'Прибыль {result}')
elif viruchka < zatraty:
    result = zatraty - viruchka
    print(f'Предприятие работает с убытком {result}')
else:
    result = 0
    print('Предприятие работает с нулевой рентабельностью')

rentabilnost = result / viruchka
print(f'Рентабельность составляет {rentabilnost}')
prib_for_one = result / kolv_sotr
print(f'Прибыль в расчете на одного сотрудника {prib_for_one} ')
