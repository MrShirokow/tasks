"""
Дан набор прямоугольников. Нужно для каждого из них посчитать, какое количество прямоугольников пересекает текущий прямоугольник
"""


from collections import defaultdict


class Rectangle:
    def __init__(self, left: int, top: int, right: int, bottom: int):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


def check_coordinates_intersect(left1: int, right2: int, top1: int, bottom2: int) -> bool:
    return left1 < right2 and top1 < bottom2


def are_intersect(r1: Rectangle, r2: Rectangle) -> bool:
    return (
        check_coordinates_intersect(r1.left, r2.right, r1.top, r2.bottom) and 
        check_coordinates_intersect(r2.left, r1.right, r2.top, r1.bottom)
    )


def fill_counters(rectangles):
    length = len(rectangles)
    counters = defaultdict(list)
    current = 0
    while True:
        if current == length:
            break
        for i in range(length):
            if current == i:
                continue
            if i not in counters[current]:
                if are_intersect(rectangles[current], rectangles[i]):
                    counters[current].append(i)
                    counters[i].append(current)
        current += 1
    return counters


def main():
    rectangles = tuple(Rectangle(*(int(c) for c in input().split())) for _ in range(int(input())))
    for value in fill_counters(rectangles).values():
        print(len(value))


if __name__ == '__main__':
    main()
