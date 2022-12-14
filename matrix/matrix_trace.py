'''
                                        След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали. 
Напишите программу, которая выводит след заданной квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.
'''


n = int(input())
matrix = [input().split() for _ in range(n)]
result = sum([int(matrix[x][x]) for x in range(n)])
print(result)