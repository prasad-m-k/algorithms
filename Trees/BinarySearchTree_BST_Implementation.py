class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if root is None:
        return

    print(root.info, end = " ")
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)



tree = BinarySearchTree()
print("Enter count of nodes:")
t = int(input())

print("Enter nodes with space separation:")
arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])


preOrder(tree.root)
print()

from collections import deque

def height(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    height = 0
    while (queue):
        curr = queue.pop()
        if curr.left or curr.right:
            height += 1
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
             
    
    return height


print(height(tree.root))