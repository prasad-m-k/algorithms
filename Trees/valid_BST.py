class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
 
    def inorder(self, n):
        if n.left:
            self.inorder(n.left)
        if n:
            print(n.val)
        if n.right:
            self.inorder(n.right)

    def preorder(self, n):
        if n:
            print("\t\t", n.val)
        if n.left:
            self.preorder(n.val)
        if n.right:
            self.preoder("\t\t\t\t",n.val)

    def __isValidHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        print(f" {low} < {val} < {high}")
        return ((low < val and val < high) and
                self.__isValidHelper(n.left,low,n.val) and
                self.__isValidHelper(n.right,n.val,high))
        
    def isValid(self, n):
        return self.__isValidHelper(n, float('-inf'), float('inf'))
        
 
 
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(node.isValid(node))
node.left.left=Node(2)
node.left.right=Node(3)
node.right.right=Node(9)
print(node.isValid(node))
#print("Tree inorder:")
node.inorder(node)