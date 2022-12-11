"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._maxPathSum = -pow(2, 31) - 1
        self.findMaxPathSum(root)
        return self._maxPathSum

    def findMaxPathSum(self, node):
        if node is None:
            return 0
        
        leftTreeSum = self.findMaxPathSum(node.left)
        rightTreeSum = self.findMaxPathSum(node.right)
        
        treeSum = max(max(leftTreeSum, rightTreeSum) + node.val, node.val)
        subtreeSum = leftTreeSum + rightTreeSum + node.val
        
        pathSum = max(treeSum, subtreeSum)
        self._maxPathSum = max(self._maxPathSum, pathSum)
        
        return treeSum
