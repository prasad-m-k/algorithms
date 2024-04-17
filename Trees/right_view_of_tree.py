from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def right_view_of_binary_tree(root):
    """
    Function to find the right view of a binary tree.
    :param root: TreeNode, the root of the binary tree
    :return: List[int], list of values seen from the right view
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_length = len(queue)
        print("level_length=",level_length)
        for i in range(level_length):
            node = queue.popleft()
            # If it's the last node in this level, add it to the result
            if i == level_length - 1:
                result.append(node.val)
            # Enqueue children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# Example usage
if __name__ == "__main__":
    # Construct the binary tree
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    # Compute the right view
    right_view = right_view_of_binary_tree(root)
    print("Right view of the binary tree:", right_view)