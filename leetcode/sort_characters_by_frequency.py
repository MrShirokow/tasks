"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        return ''.join(item[0] * item[1] for item in items)


if __name__ == '__main__':
    solution = Solution()
    assert solution.frequencySort('tree') in ('eert', 'eetr')
    assert solution.frequencySort('cccaaa') in ('aaaccc', 'cccaaa')
    assert solution.frequencySort('Aabb') in ('bbAa', 'bbaA')
    print('\nTests done\n')