from typing import Iterable
from collections import OrderedDict


def find_length_of_longest_sequence(chars: Iterable, k: int)-> int:
    right_indexes = OrderedDict()
    left_index = -1
    max_length = count = 0

    for index, char in enumerate(chars):
        if char not in right_indexes:
            count += 1
        else:
            right_indexes.pop(char)
        right_indexes[char] = index
        if count <= k:
            max_length = max(max_length, index - left_index)
        else:
            excess_char = next(iter(right_indexes.keys()))
            left_index = right_indexes[excess_char]
            right_indexes.pop(excess_char)
            count -= 1
    return max_length


assert find_length_of_longest_sequence('', 3) == 0
assert find_length_of_longest_sequence('abbabbcccbbcb', 2) == 9
assert find_length_of_longest_sequence('abbabbcccbbcb', 4) == 13
assert find_length_of_longest_sequence('aaaaaaaaaaaaaaaaaaa', 2) == 19
assert find_length_of_longest_sequence('baaaaaaaaaaaaaaaaaaab', 2) == 21
assert find_length_of_longest_sequence('cbbcbbdbc', 3) == 9
assert find_length_of_longest_sequence('ababcacdaddbbdb', 2) == 6
assert find_length_of_longest_sequence('abcdebcdecdedeea', 4) == 14
assert find_length_of_longest_sequence('aaaabbbbbccccccdddddddaaaaaaaaa', 1) == 9
assert find_length_of_longest_sequence('aaaabbbbbccccccdddddddaaaaaaaaa', 2) == 16
assert find_length_of_longest_sequence('abbcbbdbc', 3) == 8
assert find_length_of_longest_sequence('ababcacdaddbbdb', 3) == 8
assert find_length_of_longest_sequence('cabcaccbbddbcbcdbcbdbcdd', 3) == 19
assert find_length_of_longest_sequence('cabcaccbbaddabbabeabeabeabbbeeabcd', 3) == 20
