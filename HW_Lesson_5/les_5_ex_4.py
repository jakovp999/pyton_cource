with open("file_in_4.txt", "r", encoding='utf - 8') as file_in:
    text = file_in.read()

text = text.replace("One", "Один")
with open("file_out_4.txt", "w") as file_out:
    file_out.write(text)

text = text.replace("Two", "Два")
with open("file_out_4.txt", "w") as file_out:
    file_out.write(text)

text = text.replace("Three", "Три")
with open("file_out_4.txt", "w") as file_out:
    file_out.write(text)

text = text.replace("Four", "Четыре")
with open("file_out_4.txt", "w") as file_out:
    file_out.write(text)
