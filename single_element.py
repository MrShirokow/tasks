'''
На вход программе даётся список из чисел, каждое из которое, кроме одного, повторяется 2 раза. Найти число, которое встречается 1 раз.
'''

from collections import defaultdict


# Решение в лоб
def find_single_element(numbers: list[int]) -> int:
    counters = defaultdict(int)
    for number in numbers:
        counters[number] += 1
    for key in counters:
        if counters[key] == 1:
            return key


# Решение через XOR
def find_single_xor(numbers: list[int]) -> int:
    xor = 0
    for number in numbers:
        xor ^= number
    return xor


def main():
    data = [1, 2, 3, 4, 5, 6, 5, 2, 7, 3, 1, 4, 6]
    assert find_single_element(data) == 7
    assert find_single_xor(data) == 7
    print('Successfully!')


if __name__ == '__main__':
    main()
