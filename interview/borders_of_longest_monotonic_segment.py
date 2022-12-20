from typing import Optional, Callable


def get_comparison_function(previous: int, current: int) -> Callable:
    is_increasing = previous < current

    def is_ascending(previous: int, current: int) -> bool:
        return previous < current
    
    def is_descending(previous: int, current: int) -> bool:
        return previous > current
     
    return is_ascending if is_increasing else is_descending


def find_borders_of_longest_monotonic_segment(numbers: list[int]) -> Optional[tuple[int, int]]:
    if not numbers:
        return None

    length = len(numbers)
    result_left = current_left = 0
    result_right = current_right = 0
    while current_right < length - 1:
        if numbers[current_right] == numbers[current_right + 1]:
            current_left += 1
            current_right = current_left
            continue
        is_monotonic = get_comparison_function(numbers[current_left], numbers[current_right + 1])
        while current_right < length - 1 and is_monotonic(numbers[current_right], numbers[current_right + 1]):
            current_right += 1
        if current_right - current_left > result_right - result_left:
            result_left, result_right = current_left, current_right
        current_left = current_right

    return result_left, result_right


def run_tests():
    assert find_borders_of_longest_monotonic_segment([]) is None
    assert find_borders_of_longest_monotonic_segment([1]) == (0, 0)
    assert find_borders_of_longest_monotonic_segment(
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ) == (0, 0)
    assert find_borders_of_longest_monotonic_segment(
        [-3, 2, 3, 4, 5, 6, 7, 7, 8]
    ) == (0, 6)
    assert find_borders_of_longest_monotonic_segment(
        [-3, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ) == (7, 15)
    assert find_borders_of_longest_monotonic_segment(
        [-10, -9, -3, 0, 1, 2, 3, 4, 5, 6]
    ) == (0, 9)
    assert find_borders_of_longest_monotonic_segment(
        [10, 9, 8, 7, 6, 5, 3, 1]
    ) == (0, 7)
    assert find_borders_of_longest_monotonic_segment(
        [10, 9, 8, 7, 6, 5, 5, 3, 1]
    ) == (0, 5)
    assert find_borders_of_longest_monotonic_segment(
        [10, 9, 8, 7, 6, 5, 5, 3, 1, 0, -1, -2, -4]
    ) == (6, 12)
    assert find_borders_of_longest_monotonic_segment(
        [1, 2, 3, 4, 4, 1, 2, 3, 4]
    ) == (0, 3)
    assert find_borders_of_longest_monotonic_segment(
        [-4, -3, -2, -1, -4, -3, -2, -1]
    ) == (0, 3)
    assert find_borders_of_longest_monotonic_segment(
        [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    ) == (4, 9)
    assert find_borders_of_longest_monotonic_segment(
        [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, -1]
    ) == (10, 15)
    print('\ntests OK\n')


if __name__ == '__main__':
    run_tests()
