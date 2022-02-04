import codecs
# Считывание файла с нужной кодировкой
import pickle

my_file = codecs.open("zp.txt", "r", encoding='utf - 8')
content = my_file.readlines()
print(type(content))
print('Cодержимое файла:', content)
my_file.close()

a = []  # Список с числами в символном виде
b = []  # Список с числами в вещественном виде
c = []  # ЗП менее 20 тыс
my_file = codecs.open("zp.txt", "r", encoding='utf - 8')
data = my_file.read()
word = data.split()
print(word)

for x in range(1, len(word), 2):
    a.append(word[x])

b = list(map(float, a))

print('Минимальная зарплата', min(b))
min_zp = str(min(b))
my_file = codecs.open("zp.txt", "r", encoding='utf - 8')
for line in my_file:
    if min_zp in line:
        print('Самая маленькая ЗП:', line, end='')
my_file.close()

for i in b:
    if i < 20000:
        c.append(i)
print(c)
c = list(map(str, c))  # Преобразование из веществ в str

for i in c:
    my_file = codecs.open("zp.txt", "r", encoding='utf - 8')
    for lines in my_file:
        if i in lines:
            print('ЗП меньше 20000:', lines, end='')
my_file.close()

print('Максимальная зарплата', max(b))
print('Средняя зарплата', sum(b) / len(b))
