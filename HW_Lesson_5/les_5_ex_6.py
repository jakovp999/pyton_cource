result = {}
with open('subj_for_6.txt', 'r', encoding='utf - 8') as file:
    file_lines = file.readlines()

    hours = 0

for line in file_lines:
    data = line.split()
    print('Анализируемая строка', data)
    for elem in data[1:]:
        print('Срез строки', data[1:])
        num = "0"
        for i in elem:
            if i.isdigit():
                num += i
                print('Поиск цифр', num)
            else:
                print('Выход из условия поиска цифр', i)
                break
        hours += int(num)
        print('Часы сумма', hours)
    result.update({data[0].strip(':'): hours})
    print('Промежуточный результат', result)
print('Окончательный результат', result)
