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
    Assumes p and q are unique and exist in the binary tree.
    :param root: TreeNode, the root of the binary tree
    :param p: TreeNode, first node
    :param q: TreeNode, second node
    :return: TreeNode, the lowest common ancestor of p and q
    """
    if root is None:
        return None

    if root == p:
        print("returning p\n", p)
    if root == q:
        print("returning q\n", q)
        print(q)
    
    # If either p or q is the root, then root is LCA
    if root == p or root == q:
        return root
    
    # Recursively find LCA in the left and right subtree
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both left and right are non-null, this node is the LCA
    if left and right:
        print("returning root for both left and right\n", root)
        return root
    
    # Otherwise return the non-null child (either left or right)
    return left if left else right

# Example usage
if __name__ == "__main__":
    # Create the binary tree
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Find LCA of 6 and 4
    lca = lowest_common_ancestor(root, root.left.left, root.left.right.right)
    print(f"LCA of 6 and 4 is: {lca.val}")  # Output should be 5