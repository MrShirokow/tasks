'''
                                                Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n (0 < n < 1000) – количество чисел в наборе. 
В последующих n строках вводятся целые числа, составляющие набор (могут повторяться). 
Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
'''


from tkinter.tix import Tree


n = int(input())
numbers = tuple(map(int, (input() for _ in range(n))))
product = int(input())
result = False

for i in range(n):
    try:
        if numbers.index(product / numbers[i]) != i:
            result = True
            break
    except (ValueError, ZeroDivisionError):
        continue

print(['НЕТ', 'ДА'][result])