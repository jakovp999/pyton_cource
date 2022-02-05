import json

firms = {}

with open('firms_7.txt', 'r', encoding='utf - 8') as file:
    file_lines = file.readlines()

firms_with_prib = 0
all_firms_prib = 0

for line in file_lines:
    data = line.split()
    pribil = float(data[2]) - float(data[3])
    firms.update({data[0]: pribil})
    print('Промежуточная запись фирм с показателями прибыли  в словарь', firms)
    if pribil > 0:
        firms_with_prib += 1
        print('Фирм с "+" прибылью', firms_with_prib)
        all_firms_prib += pribil
        print('Всего прибыли:', pribil)

sred_prib = all_firms_prib / firms_with_prib
print('Средняя прибыль;', sred_prib)
result = [firms, {'Средняя прибыль': sred_prib}]

with open('result_json_7.txt', 'w', encoding='UTF-8') as file:
    json.dump(result, file)

with open('result_json_7.txt', 'r', encoding='UTF-8') as file:
    print('Результат считанный из файла методом JSON:', result)
