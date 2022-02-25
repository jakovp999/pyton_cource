'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, members_1, members_2):
        self.members_1 = members_1
        self.members_2 = members_2

    def __add__(self):
        add_matrix = [[i * j for j in range(3)] for i in range(3)]

        for i in range(len(self.members_1)):
            for j in range(len(self.members_2[i])):
                add_matrix[i][j] = self.members_1[i][j] + self.members_2[i][j]
        return str('  \n'.join(['\t'.join([str(elem) for elem in i]) for i in self.members_1]))

    def __str__(self):
        result_1 = str('  \n'.join(['\t'.join([str(elem) for elem in i]) for i in self.members_1]))
        result_2 = str('  \n'.join(['\t'.join([str(elem) for elem in i]) for i in self.members_2]))

        print(f'Первая матрица\n{result_1}\n\nВторая матрица')

        return result_2


my_matrix = Matrix([[12, 58, 89], [75, 26, 24], [59, 51, 73]], [[91, 73, 19], [64, 46, 31], [30, 40, 48]])
# print('Вторая матрица')
print(f'{my_matrix}\n')

print('Матрица сложения')
print(my_matrix.__add__())
