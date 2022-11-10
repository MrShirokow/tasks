'''
                                        Треугольник Паскаля 2
На вход программе подается натуральное число n. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n (n >=1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.
'''


from math import factorial 


def get_element(n: int, m: int):
    return int(factorial(n) / (factorial(m) * factorial(n - m)))


def get_row(n : int) -> list:
    return [get_element(n, m) for m in range(n + 1)]


def pascal(n: int):
    for i in range(n):
        print(*get_row(i))


n = int(input())    # Отличие от pascal.py: здесь n - количество строк для вывода, а в прошлой задаче n - номер строки (нумерация с 0)
pascal(n)