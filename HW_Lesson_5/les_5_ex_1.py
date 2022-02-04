with open("file_les_4.txt", "w", encoding='utf - 8') as file:
    input_from_user = input('Введите текст: \n')
    while input_from_user:
        file.write(f'{input_from_user}\n')
        input_from_user = input('Введите текст: \n')
