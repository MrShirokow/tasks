"""
https://leetcode.com/problems/leaf-similar-trees/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def _get_leafs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
                return

            yield from _get_leafs(node.left)
            yield from _get_leafs(node.right)

        return list(_get_leafs(root1)) == list(_get_leafs(root2))
        

if __name__ == '__main__':
    solution = Solution()
