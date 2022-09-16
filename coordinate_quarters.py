"""
Дан набор из n точек. Нужно вывести для каждой координатной четверти, сколько точек ей принадлежит 
"""


from collections import defaultdict


counter = defaultdict(lambda: defaultdict(int))

n = int(input())
for _ in range(n):
    x, y = (int(coordinate) for coordinate in input().split())
    if x == 0 or y == 0:
        continue
    counter[x > 0][y > 0] += 1

print(f'Первая четверть: {counter[1][1]}\n' 
      f'Вторая четверть: {counter[0][1]}\n' 
      f'Третья четверть: {counter[0][0]}\n' 
      f'Четвертая четверть: {counter[1][0]}')
