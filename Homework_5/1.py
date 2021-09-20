import numpy as np

""" Найти с помощью NumPy SVD для матрицы
"""

a = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])
u, s, w = np.linalg.svd(a)
v = w.T
d = np.zeros_like(a, dtype=float)
d[np.diag_indices(min(a.shape))] = s
print(f"Матрица U:\n{u}\nМатрица V:\n{v}\nМатрица D:\n{d}")
print("Проверка:\n", np.dot(np.dot(u, d), v.T))
