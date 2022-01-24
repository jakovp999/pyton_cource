strok_user = input('Введите несколько слов разделенных пробелами:'            )
print(strok_user)
spisok_user = strok_user.split( )
print(spisok_user)
len_spisok = len(spisok_user)
for j in range(len_spisok):
    print(f'{(j+1)*10}, {(spisok_user[j])[0:10]}')
    



