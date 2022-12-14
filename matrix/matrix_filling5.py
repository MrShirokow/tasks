"""
                        Заполнение 5
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n x m 
и заполняет её числами от 1 до n * m в соответствии с образцом:
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.
"""

n, m = map(int, input().split())
matrix = [[(i + j) % m + 1 for j in range(m)] for i in range(n)]
for row in matrix:
    print(*row)