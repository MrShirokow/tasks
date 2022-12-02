"""
Написать функцию, которая считает скалярное произведение двух упакованных векторов.
[(1, 3), [2, 4]] -> [1, 1, 1, 2, 2, 2, 2]
Гарантируется, что 2 вектора в распакованном виде имеют одинаковую длину.
"""


def calculate_scalar(vector1: list, vector2: list) -> int:
    pointer1, pointer2 = 0, 0
    carry1, carry2 = 0, 0
    scalar = 0
    while pointer1 < len(vector1):  # достаточно проверить только один указатель, т.к. по условию гарантируется, что векторы одинаковой длины
        if vector1[pointer1][1] - carry1 < vector2[pointer2][1] - carry2:
            scalar += vector1[pointer1][0] * vector2[pointer2][0] * (vector1[pointer1][1] - carry1)
            carry2 += vector1[pointer1][1] - carry1
            carry1 = 0
            pointer1 += 1
        elif vector2[pointer2][1] - carry2 < vector1[pointer1][1] - carry1:
            scalar += vector1[pointer1][0] * vector2[pointer2][0] * (vector2[pointer2][1] - carry2)
            carry1 += vector2[pointer2][1] - carry2
            carry2 = 0
            pointer2 += 1
        else:
            scalar += vector1[pointer1][0] * vector2[pointer2][0] * (vector2[pointer2][1] - carry2)
            carry1, carry2 = 0, 0
            pointer1 += 1
            pointer2 += 1
    return scalar
            

if __name__ == '__main__':
    assert calculate_scalar([(1, 2), (2, 2)], [(1, 1), (2, 3)]) == 11   # [1, 1, 2, 2] * [1, 2, 2, 2] = 1 + 2 + 4 + 4 = 11
    assert calculate_scalar([(1, 3), (2, 3)], [(1, 1), (2, 3), (3, 2)]) == 21   # [1, 1, 1, 2, 2, 2] * [1, 2, 2, 2, 3, 3] = 1 + 2 + 2 + 4 + 6 + 6 = 21
    assert calculate_scalar([(3, 5)], [(1, 1), (2, 2), (3, 1), (4, 1)]) == 36   # [3, 3, 3, 3, 3] * [1, 2, 2, 3, 4] = 3 + 6 + 6 + 9 + 12 = 36
    assert calculate_scalar([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], [(1, 12), (2, 3)]) == 70   # 1 + 2 + 2 + 3 + 3 + 3 + 4 + 4 + 4 + 4 + 5 + 5 + 10 + 10 + 10 = 70
    print('\nTests done\n')
