
#https://leetcode.com/problems/closest-binary-search-tree-value/

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import List, Optional

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        
        return closest

root = TreeNode(3,TreeNode(TreeNode(9), None, None),TreeNode(20, TreeNode(15),TreeNode(7)))
target = 3.714286
root = TreeNode(4,TreeNode(2,TreeNode(1,None,None),TreeNode(3,None,None)),TreeNode(5,None,None))

print(Solution().closestValue(root,target))