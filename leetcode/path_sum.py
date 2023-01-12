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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _hasPathSum(node: Optional[TreeNode], current_sum: int) -> bool:
            if not node:
                return False
            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum
            return _hasPathSum(node.left, current_sum) or _hasPathSum(node.right, current_sum)
        return _hasPathSum(root, 0)
            

if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(
        val=5,
        left=TreeNode(
            val=4,
            left=TreeNode(
                val=11,
                left=TreeNode(
                    val=7
                ),
                right=TreeNode(
                    val=2
                )
            ),
        ),
        right=TreeNode(
            val=8,
            left=TreeNode(
                val=13
            ),
            right=TreeNode(
                val=4,
                right=TreeNode(
                    val=1
                )
            )
        )
    )
    assert solution.hasPathSum(tree, 22)
