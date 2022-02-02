from sys import argv
from itertools import count, cycle

# number_end последнее число в итераторе count
# spisok список для итератора cycle
# povtor колличество выводимых символов для итератора cycle

number_end = int(input('Введите конец списка'))
spisok = input('Вндите символы для повторяющнгося списка')
povtor = int(input('Введите колличество повторов '))
count_spis = count()
cycle_spis = cycle(spisok)

for el in count(0):
    if el > number_end:
        break
    else:
        print(el)
print("Результат в виде списка:", [next(count_spis) for el in range(number_end+1)])

c = 0
for el_1 in cycle(spisok):
    if c == int(povtor):
        break
    print(el_1)
    c += 1

print("Результат в виде списка:", [next(cycle_spis) for el_1 in range(0, povtor)])
