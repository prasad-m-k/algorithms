import typing

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root: Node):
  # Fill this in.
  if root.val == PLUS:
      return evaluate( root.left) + evaluate(root.right)
  elif root.val == MINUS:
      return evaluate (root.left) - evaluate(root.right)
  elif root.val == TIMES:
      return evaluate (root.left) * evaluate(root.right)
  elif root.val == DIVIDE:
      return evaluate (root.left) / evaluate(root.right)
  else:
      return root.val
  

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print (evaluate(tree))
# 45
