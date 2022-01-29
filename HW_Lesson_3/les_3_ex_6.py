def int_func(vvod_list):
    result = vvod_list.capitalize()
    result_1 = vvod_list.title()

    return result, result_1

vvod_list = input('Введите что нибудь латинскими маленькими буквами: ')
one_word, some_word = int_func(vvod_list)
print(one_word)

vvod_list = input('Введите несколько слов разделенными пробелами латинскими маленькими буквами: ')
one_word, some_word = int_func(vvod_list)
print(some_word)



