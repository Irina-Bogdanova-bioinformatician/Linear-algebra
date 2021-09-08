import numpy as np

""" Задание: написать на Python функцию для перемножения двух произвольных матриц, не используя NumPy.

    Создали функцию matrix_multiplication(a, b), принимающую на вход 2 матрицы, каждая из которых
    представляет собой "список списков", и возвращающую матрицу, являющуюся их произведением. Если число столбцов
    в первой матрице не равно числу строк во второй, функция возвращает сообщение о невозможности осуществления
    такой операции.
    
    Используем библиотеку numpy для проверки работы функции.
"""


def matrix_multiplication(a, b):
    if len(b) != len(a[0]):
        print("Невозможно выполнить операцию. Количество столбцов в первой матрице должно совпадать с "
              "количеством строк во второй матрице")
    else:
        helper_matrix = [[el] * len(b[0]) for el in a]
        transp_b = [list(i) for i in zip(*b)]
        index = 0
        new_line = []
        new_matrix = []
        for el in helper_matrix:
            for i in el:
                new_line.append([a * b for a, b in zip(i, transp_b[index])])
                index += 1
            new_line2 = [sum(elements) for elements in new_line]
            new_matrix.append(new_line2)
            index = 0
            new_line.clear()
        helper_matrix.clear()
        return new_matrix


""" Проверим, как работает функция.
"""

x = [[1, 0], [2, 1], [10, 5]]
y = [[2, 0, 0], [0, 0, 1]]
print("Произведение матриц (X*Y), полученное с помощью функции matrix_multiplication:\n",
      matrix_multiplication(x, y))
x1 = np.array(x)
y1 = np.array(y)
print("Произведение матриц (X*Y), полученное с помощью библиотеки numpy:\n", x1.dot(y1))
print("Произведение матриц (Y*X), полученное с помощью функции matrix_multiplication:\n",
      matrix_multiplication(y, x))
print("Произведение матриц (Y*X), полученное с помощью библиотеки numpy:\n", y1.dot(x1))
x2 = [[2, 1, 4], [10, 5, 7]]
print(matrix_multiplication(x2, y))
