time = input('ВВедите вреря в секундах:  ')
print(time)
# print(type(time))

time_hour = int(time) // 3600
# print(time_hour)

time_min = int(time) % 3600 // 60
# print(time_min)
time_sec = int(time) % 3600 % 60
# print(time_sec)


# Проверка

# time_ver = time_hour * 3600 + time_min * 60 + time_sec
# print(time_ver)
# if time_ver!=time:
#     print('Вычесленно верно')
# else:
#     print('Ошибка')

result = f'{time_hour}:{time_min:02}:{time_sec:02}'
print(result)
