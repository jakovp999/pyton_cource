a = []
line = "abcd 3455 ijkl 56.78 ij"
for word in line.split():
    try:
        a.append(float(word))
    except ValueError:
        pass
print(a)

word = u'привет'
with io.open('/path/to/file.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')