my_file = open("new_text.txt", "r")
content = my_file.readlines()
data = my_file.read()
my_file.close()
print('Cодержимое файла:', content)

my_file = open("new_text.txt", "r")
print('Колличество строк в файле:', sum(1 for line in my_file))

word = data.split()
print('Колличество слов в фойле:', len(word))

for str, line in enumerate(content):
    word_kolich = len(line.split())
    print(f'Колличество слов в строке {str + 1} - {word_kolich}')
