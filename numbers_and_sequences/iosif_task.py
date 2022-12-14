"""
n человек, пронумерованных числами от 1 до n, стоят в кругу. 
Они начинают считаться, каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. 
Напишите программу, определяющую номер человека, который останется в кругу последним.

1. Создаем список people
2. Удаляем каждый i-ый элемент, где i = (i + k - 1) % len(people) в цикле
"""


n, k = (int(input()) for _ in range(2))
people = list(range(n))
i = 0

while len(people) > 1:
    i = (i + k - 1) % len(people)
    del people[i]

print(people[0] +  1)
