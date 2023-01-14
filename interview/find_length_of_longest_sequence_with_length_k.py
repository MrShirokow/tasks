from typing import Iterable


def find_length_of_longest_sequence(chars: Iterable, k: int) -> int:
    if not chars:
        return 0

    index_mapping = {}
    previous = None
    max_len = count = current_len = 0

    for i, e in enumerate(chars):
        if e not in index_mapping:
            index_mapping[e] = i
            previous = e
            if count < k:
                count += 1
                current_len += 1
            elif count == k:
                excess_element = get_first_element(index_mapping)
                del index_mapping[excess_element]
                current_len = i - index_mapping[get_first_element(index_mapping)] + 1
        else:
            update_index(e, previous, i, index_mapping)
            previous = e
            current_len += 1

        max_len = max(max_len, current_len)
    return max_len


def get_first_element(chars: dict):
    return min(chars, key=chars.get)


def update_index(current, previous, index: int, index_mapping: dict):
    if current != previous and previous:
        first_element = get_first_element(index_mapping)
        if previous == first_element:
            index_mapping[current] = index


assert find_length_of_longest_sequence('', 3) == 0
assert find_length_of_longest_sequence('abbabbcccbbcb', 2) == 9
assert find_length_of_longest_sequence('abbabbcccbbcb', 4) == 13
assert find_length_of_longest_sequence('aaaaaaaaaaaaaaaaaaa', 2) == 19
assert find_length_of_longest_sequence('baaaaaaaaaaaaaaaaaaab', 2) == 21
assert find_length_of_longest_sequence('abbcbbdbc', 3) == 8
assert find_length_of_longest_sequence('cbbcbbdbc', 3) == 9
assert find_length_of_longest_sequence('ababcacdaddbbdb', 2) == 6
assert find_length_of_longest_sequence('ababcacdaddbbdb', 3) == 8
assert find_length_of_longest_sequence('abcdebcdecdedeea', 4) == 14
assert find_length_of_longest_sequence('abcdebcdecdedeea', 4) == 14

