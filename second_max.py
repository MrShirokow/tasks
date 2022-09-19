def find_second_max(numbers: list[int]) -> int | None:
    second_max = absolute_max = float('-inf')
    for number in numbers:
        if number == absolute_max:
            continue
        elif number > absolute_max:
            second_max = absolute_max
            absolute_max = number
        elif number > second_max:
            second_max = number
    return second_max if second_max > float('-inf') else None


def main():
    result = find_second_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong {result}'
    result = find_second_max([100, 100, 99])
    assert result == 99, f'Wrong {result}'
    result = find_second_max([100, 100, 100, 0])
    assert result == 0, f'Wrong {result}'
    result = find_second_max([100, 100])
    assert result is None, f'Wrong {result}'
    result = find_second_max([1])
    assert result is None, f'Wrong {result}'
    result = find_second_max([])
    assert result is None, f'Wrong {result}'
    print('Succesfully!')


if __name__ == '__main__':
    main()
