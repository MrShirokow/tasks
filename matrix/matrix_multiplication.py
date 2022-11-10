"""
                Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы первой матрицы, 
затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""


n, m = map(int, input().split())
matrix_1 = [[int(e) for e in input().split()] for _ in range(n)]
input()
m, k = map(int, input().split())
matrix_2 = [[int(e) for e in input().split()] for _ in range(m)]
zip_matrix_2 = list(zip(*matrix_2))

multi_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip_matrix_2] for row in matrix_1]
for row in multi_matrix:
    print(*row)