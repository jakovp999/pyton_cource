from sys import argv
from itertools import count
from itertools import cycle

# number_one первое число в итераторе count
# number_end последнее число в итераторе count
# spisok список для итератора cycle
# povtor колличество выводимых символов для итератора cycle c 0
# Строка запуска   python les_4_ex_6.py  3 10 Привет_страна 20
script_names, number_one, number_end, spisok, povtor = argv
for el in count(int(number_one)):
    if el > int(number_end):
        break
    else:
        print(el)

c = 0
for el_1 in cycle(spisok):
    if c > int(povtor):
        break
    print(el_1)
    c += 1
