# Функция n факториал
def fac(n):
    itog = 1
    if n == 1:
        yield 1

    for i in range(1, n + 1):
        itog *= i
        yield itog


print(fac(4))
n = 4

for el in fac(n):
    print(el)
