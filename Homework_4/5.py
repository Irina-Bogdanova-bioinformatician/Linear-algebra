import copy

""" Функция cramer_method() решает СЛАУ методом Крамера, используя функции submatrix() и determinant(),
    которые вычисляют миноры и определитель матрицы соответственно.
    На вход функция получает матрицу коэффициентов и вектор b - и то, и другое в виде списка списков.
    Возвращает список с ршениями СЛАУ.
"""


def submatrix(m, c):
    b = [[1] * len(m) for i in range(len(m))]
    for l in range(len(m)):
        for k in range(len(m)):
            b[l][k] = m[l][k]
    b.pop(0)
    for i in range(len(b)):
        b[i].pop(c)
    return b


def determinant(m):
    x = 0
    if len(m) != len(m[0]):
        return "Матрица не квадратная"
    else:
        if len(m) <= 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        else:
            for i in range(len(m)):
                x = x + ((-1) ** i) * m[0][i] * determinant(submatrix(m, i))
    return x


def cramer_method(m, b):
    a = determinant(m)
    if a == "Матрица не квадратная":
        print("Невозможно выполнить операцию. Количество столбцов в первой матрице должно совпадать с "
              "количеством строк во второй матрице")
    elif a == 0:
        print("Определитель матрицы коэффициентов равен нулю - решение СЛАУ методом Крамера невозможно")
    else:
        counter = 0
        det_list = []
        while counter < len(m):
            n = 0
            m_new = copy.deepcopy(m)
            for el in m_new:
                el[counter] = b[0][n]
                n += 1
            det_list.append(determinant(m_new))
            counter += 1
            m_new.clear()
        results_list = [i / a for i in det_list]
        return results_list


r = [[1, -2], [3, -4]]
d = [[1, 7]]
print(cramer_method(r, d))

e = [[2, -1, 5], [1, 1, -3], [2, 4, 1]]
f = [[10, -2, 1]]
print(cramer_method(e, f))
