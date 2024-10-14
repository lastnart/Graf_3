import numpy as np

def input_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        row_input = input(f"Введите строку {i + 1} из {n} элементов (0 или 1): ")
        while len(row_input) != n or any(c not in '01' for c in row_input):
            row_input = input(f"Ошибка! Введите строку из {n} элементов (0 или 1): ")
        matrix[i] = [int(c) for c in row_input]  # Преобразуем строку в целые числа
    return matrix

def matrix_multiply(A, B):
    return np.dot(A, B)

def reachability_matrix(matrix, d, n):
    reach_matrices = [matrix]
    for length in range(1, d):  # Изменяем цикл до диаметра d
        new_matrix = matrix_multiply(reach_matrices[-1], matrix)
        reach_matrices.append(new_matrix)
    return reach_matrices

def main():
    n = int(input("Введите размерность матрицы (n): "))
    d = int(input("Введите диаметр матрицы (d): "))  # Запрашиваем диаметр матрицы
    matrix = input_matrix(n)

    reach_matrices = reachability_matrix(matrix, d, n)

    print(f"\nМатрицы достижимости до диаметра {d}:\n")
    sum_matrix = np.zeros((n, n), dtype=int)

    for length in range(d):
        print(f"Матрица достижимости для цепей длины {length + 1}:\n{(reach_matrices[length] > 0).astype(int)}\n")
        sum_matrix += reach_matrices[length]

    # Выводим сумму рассчитанных матриц
    print(f"Сумма всех посчитанных матриц:\n{(sum_matrix > 0).astype(int)}\n")

    # Приведение суммарной матрицы к диагональному виду
    result_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        if sum_matrix[i, i] > 0:  # Если есть достижимость самосвязи, то записываем
            result_matrix[i, i] = 1
        # Другие элементы остаются 0

    print(f"Финальная диагональная матрица достижимости (S1 + S2 + ... + Sd):\n{result_matrix}\n")

if __name__ == '__main__':
    main()
