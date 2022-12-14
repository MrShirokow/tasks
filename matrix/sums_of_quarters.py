'''
                                    Суммы четвертей
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.
'''


from collections import defaultdict


n = int(input())
counter = defaultdict(lambda: defaultdict(int))
matrix = [[int(e) for e in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j:
            continue
        counter[i > j][i > n - 1 - j] += matrix[i][j]

print(f'''
Верхняя четверть: {counter[0][0]}
Правая четверть: {counter[0][1]}
Нижняя четверть: {counter[1][1]}
Левая четверть: {counter[1][0]}
''')
