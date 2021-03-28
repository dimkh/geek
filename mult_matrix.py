import sys
import numpy as np        # Для проверки

# Матрицы заданы заранее (для демонстрации)
# Если нужен ручной ввод - поставить False
AUTO_WORK = True

if AUTO_WORK:
    A_row = 2
    A_col = 3
    B_row = 3
    B_col = 2
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[6, 5], [4, 3], [2, 1]]
else:
    # Уточняем размерность матриц
    A_row = int(input('Введите количество строк 1-й матрицы (A): '))
    A_col = int(input('Введите количество столбцов 1-й матрицы (A): '))
    B_row = int(input('Введите количество строк 2-й матрицы (B): '))
    B_col = int(input('Введите количество столбцов 2-й матрицы (B): '))

    # Проверка размерности
    if A_col != B_row:
        print('Невозможно выполнить умножение матриц заданного размера!')
        sys.exit()

    # Создание матриц
    A = [[0] * A_col for i in range(A_row)]
    B = [[0] * B_col for j in range(B_row)]

    # Заполнение матриц
    print("\nЗаполните поэлементно матрицу А")
    for i in range(A_row):
        for j in range(A_col):
            A[i][j] = int(input(f"Введите элемент [{i},{j}]: "))

    print("\nЗаполните поэлементно матрицу B")
    for i in range(B_row):
        for j in range(B_col):
            B[i][j] = int(input(f"Введите элемент [{i},{j}]: "))

# Создание итоговой матрицы
R = [[0] * A_row for i in range(B_col)]

# Перемножение матриц
for i in range(A_row):
    for j in range(B_col):
        for k in range(A_col):
            R[i][j] += A[i][k] * B[k][j]

print("Матрица A:")
print(A)
print("Матрица B:")
print(B)
print("\nРезультат произведения матриц A и B:")
print(R)
print("\nПроверка произведения с помощью numpy:")
print(np.dot(A, B))
