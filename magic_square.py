"""
                                        Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n x n, составленная из всех чисел 1, 2, 3, ...,  n^2 
так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. 
Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, 
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
"""


def is_magic_square(matrix, n):
    numbers = {e + 1 for e in range(n ** 2)}
    matrix_numbers = [e for row in matrix for e in row]
    if len(numbers) != len(matrix_numbers) or set(matrix_numbers) != numbers:
        return False

    sum_main_diagonal = 0
    sum_minor_diagonal = 0
    for i in range(n):
        sum_main_diagonal += matrix[i][i]
        sum_minor_diagonal += matrix[i][n - i - 1]
    if sum_main_diagonal != sum_minor_diagonal:
        return False

    for i in range(n):
        sum_rows = 0
        sum_columns = 0
        for j in range(n):
            sum_rows += matrix[i][j]
            sum_columns += matrix[j][i]
        if not (sum_rows == sum_columns == sum_main_diagonal):
            return False
    return True


n = int(input())
matrix = [[int(e) for e in input().split()] for _ in range(n)]
print(['NO', 'YES'][is_magic_square(matrix, n)])
