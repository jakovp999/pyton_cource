chislo = int(input('Введите число'))

chislo_max = chislo % 10
# print(chislo_max)
chislo = chislo // 10
# print(chislo)

while chislo > 0:
    if chislo_max < chislo % 10:
        chislo_max = chislo % 10
    chislo = chislo // 10

print('Максимально число')
print(chislo_max)
