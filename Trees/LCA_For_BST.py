from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        s="\t" + str( self.val)+"\n"
        s += "\t/\\"
        if self.left:
            s+="\n       "+str(self.left.val)
        else:
            s+="\n    None"
        if self.right:
            s += "  " +str(self.right.val)
        else:
            s+="  None"
        return s

class BstNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if self.right is None:
                self.right = BstNode(val)
            else:
                self.right.insert(val)
        else: # self.val > val
            if self.left is None:
                self.left = BstNode(val)
            else:
                self.left.insert(val)

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


    def lowest_common_ancestor(self, root, p, q):
        """
        Function to find the lowest common ancestor in a BST.
        :param root: TreeNode, the root of the BST
        :param p: TreeNode, first node
        :param q: TreeNode, second node
        :return: TreeNode, the lowest common ancestor of p and q
        """
        current = root
        while current:
            if p < current.val and q < current.val:
                current = current.left
            elif p > current.val and q > current.val:
                current = current.right
            else:
                #print(current.val)
                return current.val  # This is the split point, so it's the LCA

    def height(self, root):
        height = 0
        if root is None:
            return height
        ldepth=self.height(root.left)
        rdepth=self.height(root.right)
    
        return max(rdepth,ldepth) + 1

# Example usage
if __name__ == "__main__":
    # Create the BST
    #        20
    #       /  \
    #     10    30
    #    /  \
    #   5   15
    #      /  \
    #     12   18
    #root = TreeNode(20)
    #root.left = TreeNode(10)
    #root.right = TreeNode(30)
    #root.left.left = TreeNode(5)
    #root.left.right = TreeNode(15)
    #root.left.right.left = TreeNode(12)
    #root.left.right.right = TreeNode(18)
    #root.left.right.right.left = TreeNode(20)
    #root.right.left = TreeNode(32)
    #root.right.left.right = TreeNode(36)
    #root.right.left.right.left = TreeNode(38)
    
    # Find LCA of 5 and 18
    #lca = lowest_common_ancestor(root, root.left.left, root.left.right.right)
    #print(f"LCA of 5 and 18 is: {lca.val}")  # Output should be 10
    
    #print("height=", height(root))
    n = BstNode(0)
    x = [1, 2, 3, 5, 4, 7, 9, 10, 22, 30]
    for i in x:
        n.insert(i)

    n.display()
    print("height=", n.height(n))
    print(n.lowest_common_ancestor(n,10,30))