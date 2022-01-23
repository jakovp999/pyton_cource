spisok = [1,2.2,0o750, None, True, 'hello', ('spam', 'one', 0xaf), {'color':'blue'}]
print(spisok)
len_spis = len(spisok)
print(len_spis)
i = 0
for i in range(len_spis):
    type_chlen = type(spisok[i])
    print (f'{i} член {type_chlen}')

