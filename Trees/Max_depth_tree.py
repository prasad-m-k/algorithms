#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import List, Optional
from collections import deque
class Solution:
    def maxDepth_dfs_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level=0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
    
        return level
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth= stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
            
            return res


##root = [3,9,20,null,null,15,7]
root = TreeNode(3,TreeNode(TreeNode(9), None, None),TreeNode(20, TreeNode(15),TreeNode(7)))
##root = [1,None,2]
root = TreeNode(1,None, TreeNode(TreeNode(2), None, None))

print(Solution().maxDepth(root))    