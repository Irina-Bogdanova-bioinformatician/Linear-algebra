import numpy as np

""" Для матрицы из предыдущего задания найти:
    а) евклидову норму;
    б) норму Фробениуса.
"""

a = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])
u, s, w = np.linalg.svd(a)
d = np.zeros_like(a, dtype=float)
d[np.diag_indices(min(a.shape))] = s
print("Норма Евклида (первый диагональный элемент матрицы D):", d[0][0])
print("Норма Евклида, рассчитанная с помощью numpy.linalg.norm:", np.linalg.norm(a, ord=2))
frob_norm = np.sqrt(sum([i ** 2 for i in s]))
b = 0
for el in a:
    b += sum([i ** 2 for i in el])
frob_norm_2 = np.sqrt(b)
print("Норма Фробениуса (квадратный корень из суммы квадратов всех элементов матрицы А):", frob_norm_2)
print("Норма Фробениуса (квадратный корень из суммы квадратов диагональных элементов матрицы D):", frob_norm)
print("Норма Фробениуса, рассчитанная с помощью numpy.linalg.norm:", np.linalg.norm(a))
