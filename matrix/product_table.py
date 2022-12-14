'''
                                Таблица умножения
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. 
Создайте матрицу mult размером n x m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа (для этого используйте строковый метод ljust()).
'''


n, m = (int(input()) for _ in range(2))
mult = [[str(i * j).ljust(3) for j in range(m)] for i in range(n)]


for row in mult:
    print(*row)
