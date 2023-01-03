"""
https://leetcode.com/problems/delete-columns-to-make-sorted/
"""


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        packs = zip(*strs)
        for pack in packs:
            if pack != tuple(sorted(pack)):
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.minDeletionSize(["cba","daf","ghi"]) == 1
    assert solution.minDeletionSize(["a","b"]) == 0
    assert solution.minDeletionSize(["zyx","wvu","tsr"]) == 3
    print('\ntests OK\n')
