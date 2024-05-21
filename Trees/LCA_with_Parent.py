
# Definition for a Node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def lowestCommonAncestor_2(self, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes = set()
        
        while p:
            nodes.add(p)
            p = p.parent
            
        while (q not in nodes):
            q = q.parent
            
        return q
    
    def lowestCommonAncestor(self, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pointer1, pointer2 = p, q
        
        # Continue until both pointers find the common ancestor
        while pointer1 != pointer2:
            # If pointer1 reaches root (None), switch to q. Else, move to its parent.
            pointer1 = pointer1.parent if pointer1 else q
            
            # If pointer2 reaches root (None), switch to p. Else, move to its parent.
            pointer2 = pointer2.parent if pointer2 else p
            
        return pointer1    
            


root = TreeNode(3)
root.left = TreeNode(5)
root.left.parent=root  #3
p = root.right = TreeNode(1)
root.right.parent=root #3

root.left.left = TreeNode(6)
root.left.left.parent = root.left
q = root.left.right = TreeNode(2)
root.left.right.parent = root.left

root.left.right.left = TreeNode(7)
root.left.right.left.parent = root.left.right

root.left.right.right = TreeNode(4)
root.left.right.right.parent = root.left.right

root.right.left = TreeNode(0)
root.right.left.parent = root.right
root.right.right = TreeNode(8)
root.right.right.parent = root.right

root.display()

print(f"parent of {p.val} and {q.val} = {Solution().lowestCommonAncestor(p,q).val}")