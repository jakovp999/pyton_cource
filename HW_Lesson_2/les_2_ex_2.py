len_spisok = int(input('Введите колличество элементов списка:   '))
spisok = []
for i in range(len_spisok):
    element = input(f'Введите значение {i} элемента')
    spisok.append(element)
print(spisok)
for i in range(0,len_spisok - 1, 2):
    spisok[i], spisok[i+1] = spisok[i+1], spisok[i]

print(spisok)







