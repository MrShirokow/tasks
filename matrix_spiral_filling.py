"""
                                Заполнение спиралью 😈😈
На вход программе подаются два натуральных числа n и m. Напишите программу, которая 
создает матрицу размером n x m, заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.
"""


n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
count = (min(n, m) + 1) // 2
number = 1
start_n, end_n = 0, n - 1
start_m, end_m = 0, m - 1

for i in range(count):
    for j in range(start_m, end_m + 1):
        matrix[i][j] = number
        number += 1
    if n == 1:
        break
    for j in range(start_n + 1, end_n + 1):
        matrix[j][end_m] = number
        number += 1
    if m == 1:
        break
    for j in range(end_m - 1, start_m - 1, -1):
        matrix[end_n][j] = number
        number += 1
    for j in range(end_n - 1, start_n, -1):
        matrix[j][start_n] = number
        number += 1
    start_n += 1
    start_m += 1
    end_m -= 1
    end_n -= 1

    
for row in matrix:
    print(*row, sep='\t')
