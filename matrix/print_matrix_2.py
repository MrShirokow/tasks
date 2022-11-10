'''
                                            Вывести матрицу 2
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, 
но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.
'''


def print_matrix_by_rows(matrix: list[list], rows: int, columns: int):
    for row in range(rows):
        for column in range(columns):
            print(matrix[row][column], end=' ')
        print()


def print_matrix_by_columns(matrix: list[list], rows: int, columns: int):
    for column in range(columns):
        for row in range(rows):
            print(matrix[row][column], end=' ')
        print()        


n, m = (int(input()) for _ in range(2))
matrix = [[input() for _ in range(m)] for _ in range(n)]

print_matrix_by_rows(matrix, n, m)
print()
print_matrix_by_columns(matrix, n, m)