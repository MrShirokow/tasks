
from typing import List
from collections import Counter


def two_sum_all(nums: List[int], target: int):
    counter = Counter(nums)
    seen = set()

    for value in counter:
        if target - value in counter and target - value not in seen:
            seen.add(value)
            n = counter[value] * counter[target - value]
            for _ in range(n):
                yield value, target - value


if __name__ == '__main__':
    assert list(two_sum_all([4, 1, 4, 1, 3, 3, 2, 2], 5)) == [(4,1), (4,1), (4,1), (4,1), (3,2), (3,2), (3,2), (3,2)]
    assert list(two_sum_all([4, 1, 4, 1, 3, 3, 2, 2], 0)) == []
    assert list(two_sum_all([9, 0, 1, 8, 8, 1, 0], 9)) == [(9, 0), (9, 0), (1, 8), (1, 8), (1, 8), (1, 8)]
    assert list(two_sum_all([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3], 3)) == [(2, 1) for _ in range(11)]
    print('\nTests done\n')
