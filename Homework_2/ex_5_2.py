import numpy as np

""" Задание: написать на Python функцию для перемножения двух произвольных матриц, не используя NumPy.

    Представленная в этом файле функция matrix_multiplication() работает так же, как функция 
    matrix_multiplication() в файле ex_5.py. Однако здесь используется промежуточный список helper_list, 
    занимающий меньше места, чем промежуточная матрица helper_matrix в файле ex_5.py.

    Используем библиотеку numpy для проверки работы функции.
"""


def matrix_multiplication(a, b):
    if len(b) != len(a[0]):
        print("Невозможно выполнить операцию. Количество столбцов в первой матрице должно совпадать с "
              "количеством строк во второй матрице")
    else:
        transp_b = [list(k) for k in zip(*b)]
        new_line = []
        helper_list = []
        new_matrix = []
        count = 0
        for el in a:
            helper_list.append([el] * len(b[0]))
            for s in helper_list[0]:
                new_line.append([a * b for a, b in zip(s, transp_b[count])])
                count += 1
            new_line_2 = [sum(elements) for elements in new_line]
            new_matrix.append(new_line_2)
            count = 0
            new_line.clear()
            helper_list.clear()
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
