viruchka = int(input('Введите выручку предприятия:  '))
zatraty = int(input('Введите затраты предприятия:   '))

if viruchka > zatraty:
    result = viruchka - zatraty
    print(f'Прибыль {result}')
elif viruchka < zatraty:
    result = zatraty - viruchka
    print(f'Предприятие работает с убытком {result}')
else:
    print('Предприятие работает с нулевой рентабельностью')

