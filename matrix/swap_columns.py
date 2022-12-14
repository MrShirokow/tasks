'''
                        Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице, 
затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.         
'''


n, m = (int(input()) for _ in range(2))
matrix = [[int(e) for e in input().split()] for _ in range(n)]
i, j = map(int, input().split())

for row in range(n):
    matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]

[print(*row) for row in matrix]
