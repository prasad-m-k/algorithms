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


def lowest_common_ancestor(root, p, q):
    """
    Function to find the lowest common ancestor in a BST.
    :param root: TreeNode, the root of the BST
    :param p: TreeNode, first node
    :param q: TreeNode, second node
    :return: TreeNode, the lowest common ancestor of p and q
    """
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            print(current)
            return current  # This is the split point, so it's the LCA

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
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.left.right.left = TreeNode(12)
    root.left.right.right = TreeNode(18)

    # Find LCA of 5 and 18
    lca = lowest_common_ancestor(root, root.left.left, root.left.right.right)
    print(f"LCA of 5 and 18 is: {lca.val}")  # Output should be 10