my_file = open("new_text.txt", "r")
content = my_file.readlines()
print('Cодержимое файла:', content)
my_file.close()

my_file = open("new_text.txt", "r")
print('Колличество строк в файле:', sum(1 for line in my_file))
my_file.close()

my_file = open("new_text.txt", "r")
data = my_file.read()
word = data.split()
print('Колличество слов в фойле:', len(word))
my_file.close()
