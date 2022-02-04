with open("file_in_4.txt", "r", encoding='utf - 8') as file_in, open("file_out_4.txt", "w") as file_out:
    text = file_in.read()
    text = text.replace("One", "Один")
    file_out.write(text)
    text = text.replace("Two", "Два")
    file_out.write(text)
    text = text.replace("Three", "Три")
    file_out.write(text)
    text = text.replace("Four", "Четыре")
with open("file_out_4.txt", "w") as file_out:
    file_out.write(text)



#Второй способ
dict_num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("file_in_4.txt", "r", encoding='utf - 8') as file_in, open("file_out_4_1.txt", "w") as file_out:
    file_lines = file_in.readlines()
    for line in file_lines:
        str_spl = line.split()
        text = dict_num.get(str_spl[0]) #Первое слово в строке англ цифра
        file_out.write(f'{line.replace(str_spl[0], text)}')
