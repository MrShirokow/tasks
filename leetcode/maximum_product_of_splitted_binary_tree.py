"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def _getSum(node: Optional[TreeNode]) -> int: 
            if not node: 
                return 0 
            current_sum = node.val + _getSum(node.left) + _getSum(node.right)
            sums.append(current_sum)
            return current_sum
        
        total = _getSum(root)
        return int(max((total - x) * x for x in sums) % (1e9 + 7))
        

if __name__ == '__main__':
    solution = Solution()
