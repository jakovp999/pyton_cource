a = int(input('Введите начальное значение (км):  '))
b = int(input('Введите желаемый результат (км):   '))

s = a  # растояние пробегаемое каждый день
i = 1  # день занятия
print(f'В {i}-й день {s}')
while s < b:
    s = s * 1.1
    i = i + 1
    s_okr = round(s, 2)
    print(f'В {i}-й день {s_okr}')
print(f'Ответ: на {i} день спортсмен достигнет результата — не менее {b} км. в день')
