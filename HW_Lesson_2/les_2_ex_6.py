#Ддя проверки авнлитикм, чтобы не вводить товары каждый раз
tovars = [
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]


kolichestvo_tovara = int(input("Введите колличество товаров которые будете вводить: "))
marks = {}
i = 4
for i in range(4,4+kolichestvo_tovara):
    tovar_name = input("Введите наименование товара: ")
    tovar_price = int(input("Введите цену товара: "))
    tovar_kol = int(input("Введите количество товара: "))
    tovar_ed = input("Введите единицу измерения товара: ")
    marks['название'] = tovar_name
    marks['цена'] = tovar_price
    marks['количество'] = tovar_kol
    marks['eд'] = tovar_ed
    tovar_cort = (i,marks)
    # print(tovar_cort)
    tovars.append(tovar_cort)
    print(tovars)

marks_temp = {}
result_analiz = {}
i = 0
len_tovars = len(tovars)

for i in range(0,len_tovars):
    marks_temp = tovars[i][1]
    print(f' 1й шаг {tovars[i][0]}, {tovars[i][1]}')
    for key, value in tovars[i][1].items():
        print(f'2й шаг key = {key}, value = {value}')
        if not result_analiz.get(key):
            result_analiz[key] = [value]
            print(f' результат поэтапно {result_analiz}')
        else:
            result_analiz[key].append(value)

for key, value in result_analiz.items():
    result_analiz[key] = list(set(value))

print(result_analiz)
