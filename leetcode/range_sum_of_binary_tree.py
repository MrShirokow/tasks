"""
https://leetcode.com/problems/range-sum-of-bst/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        def _rangeSumBST(node: Optional[TreeNode], range_sum: int):
            if not node:
                return range_sum
            if low <= node.val <= high:
                range_sum += node.val
            range_sum = _rangeSumBST(node.left, range_sum)
            range_sum = _rangeSumBST(node.right, range_sum)
            return range_sum

        range_sum = _rangeSumBST(root, range_sum)
        return range_sum
        

if __name__ == '__main__':
    solution = Solution()
