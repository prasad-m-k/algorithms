from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        if self.val:
            return(f"{self.left}  <-  {self.val}  ->  {self.right}")
        else:
            return ""
            

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right=root.right ,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

##root = [3,9,20,null,null,15,7]
root = TreeNode(3,TreeNode(TreeNode(9), None, None),TreeNode(20, TreeNode(15),TreeNode(7)))


#root = TreeNode(4,TreeNode(TreeNode(9), None, None),TreeNode(20, TreeNode(15),TreeNode(7)))
#[4,2,7,1,3,6,9]
print(root)
Solution().invertTree(root)
print(root)