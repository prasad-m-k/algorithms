#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def __recursion(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = __recursion(root.left, string)
                string = __recursion(root.right, string)
            return string
        return __recursion(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def __drecursion(L):
            if L[0] == 'None':
                L.pop(0)
                return None
            root = TreeNode(L[0])
            L.pop(0)
            root.left = __drecursion(L)
            root.right = __drecursion(L)
            return root
        data_list = data.split(',')
        root = __drecursion(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))