from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Function to perform level order traversal on a binary tree.
    :param root: TreeNode, the root of the binary tree
    :return: List[List[int]], a list of levels with the values of nodes at each level
    """
    if not root:
        return []

    results = []
    queue = deque([root])

    while queue:
        level_length = len(queue)
        current_level = []

        for _ in range(level_length):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        results.append(current_level)

    return results

# Example usage
if __name__ == "__main__":
    # Construct the binary tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Perform level order traversal
    result = level_order_traversal(root)
    print("Level order traversal of the binary tree:")
    for level in result:
        print(level)