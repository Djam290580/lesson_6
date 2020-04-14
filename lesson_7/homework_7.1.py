# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

matrix_1 = [[2, 3, 6, 1], [7, 8, 9, 4], [5, 3, 7, 0]]
matrix_2 = [[8, 5, 2, 0], [7, 4, 1, 0], [0, 5, 9, 3]]


class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return '\n'.join(map(str, self.param))

    def __add__(self, other):
        matrix_3 = []
        for i in range(len(self.param)):
            matrix_3.append([])
            for j in range(len(self.param[0])):
                matrix_3[i].append(self.param[i][j] + other.param[i][j])
        return '\n'.join(map(str, matrix_3))

mx_1 = Matrix(matrix_1)
mx_2 = Matrix(matrix_2)

print(f'Matrix_1:\n{mx_1}')
print()
print(f'Matrix_2:\n{mx_2}')
print(f'Matrix_3 = Matrix_1 + Matrix_2:\n{mx_1 + mx_2}')

# -------------------------------------------------------------------------------------------------------------------

# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))
#
#     def __add__(self, other):
#         return Matrix([self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
#             for j in range(len(self.matrix[0])))
#
# stroki = int(input('Введите количество строк и столбцов матрицы: '))
# stolbci = stroki
# matrix_1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
# matrix_2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])
# print('First matrix:\n', matrix_1, end='\n\n')
# print('Second matrix:\n', matrix_2, end='\n\n')

# ---------------------------------------------------------------------------------------------------------------------

# class Matrix:
#     def __init__(self, list_1, list_2):
#         # self.matr = [list_1, list_2]
#         self.list_1 = list_1
#         self.list_2 = list_2
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))
#
#     def __add__(self):
#         matr = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]
#
#         for i in range(len(self.list_1)):
#
#             for j in range(len(self.list_2[i])):
#                 matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
#
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
#
# my_matrix = Matrix([[5, 18, 11],
#                     [6, 17, 23],
#                     [41, 50, 9]],
#                    [[45, 8, 2],
#                     [6, 7, 93],
#                     [24, 5, 97]])
# # result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
#
# print(my_matrix.__add__())
