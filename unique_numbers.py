'''
                            Задача с собеса Яндекса
На вход программе подаётся список чисел. Нужно вывести список тех чисел, которые:
1. уникальные
2. больше числа m
'''

from collections import Counter


def get_unique_elements(numbers: list[int], m: int) -> list:
    unique_elements = [e[0] for e in Counter(numbers).items() if e[1] == 1 and e[0] > m]
    return unique_elements


def main():
    result = get_unique_elements([1, 2, 1, 2, 3, 5, 6, 6, 8, 10], 5)
    assert result == [8, 10], f'Wrong {result}'
    result = get_unique_elements([], 3)
    assert result == [], f'Wrong {result}'
    result = get_unique_elements([1, 2, 1, 2, 3, 5], 5)
    assert result == [], f'Wrong {result}'
    result = get_unique_elements([0, 0, 0, 0], 0)
    assert result == [], f'Wrong {result}'
    result = get_unique_elements([1], 0)
    assert result == [1], f'Wrong {result}'
    print('Successfully!')


if __name__ == '__main__':
    main()
