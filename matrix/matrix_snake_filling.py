"""
                        Заполнение змейкой
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n x m,
заполнив её "змейкой" в соответствии с образцом:
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.
"""

n, m = map(int, input().split())
matrix = [[str(i * m + j + 1).ljust(3) for j in range(m)][::(-1) ** i] for i in range(n)]
for row in matrix:
    print(*row)