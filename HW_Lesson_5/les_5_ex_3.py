my_file = open("zp.txt", "r", encoding='utf - 8')
data = my_file.read()

content = my_file.readlines()

print('Cодержимое файла:', content)

a = []  # Список с числами в символном виде
b = []  # Список с числами в вещественном виде
c = []  # ЗП менее 20 тыс

word = data.split()
print(word)

for x in range(1, len(word), 2):
    a.append(word[x])

b = list(map(float, a))

print('Минимальная зарплата', min(b))
min_zp = str(min(b))
for line in my_file:
    if min_zp in line:
        print('Самая маленькая ЗП:', line, end='')

for i in b:
    if i < 20000:
        c.append(i)
print(c)
c = list(map(str, c))  # Преобразование из веществ в str

for i in c:
    for lines in my_file:
        if i in lines:
            print('ЗП меньше 20000:', lines, end='')
my_file.close()

print('Максимальная зарплата', max(b))
print('Средняя зарплата', sum(b) / len(b))
