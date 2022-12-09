"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def _maxAncestorDiff(node: Optional[TreeNode], maximum: int, minimum: int) -> int:
            if not node:
                return maximum - minimum

            return max(
                _maxAncestorDiff(node.left, max(maximum, node.val), min(minimum, node.val)), 
                _maxAncestorDiff(node.right, max(maximum, node.val), min(minimum, node.val))
            )

        return _maxAncestorDiff(root, root.val, root.val)
        

if __name__ == '__main__':
    solution = Solution()
