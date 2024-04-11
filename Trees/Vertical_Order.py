

def verticalOrder(root):
    nodes = collections.defaultdict(list)
    queue = collections.deque([(root, 0)])
    while queue:
        node, pos = queue.popleft()
        if not node:
            continue
        nodes[pos].append(node.val)
        queue.append((node.left, pos-1))
        queue.append((node.right, pos+1))
    return [nodes[i] for i in sorted(nodes)]


#Could be written without sorting if we maintain low and high positions

def verticalOrder1(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    l, r, d = 0, 0, defaultdict(list)
    q = deque([(0, root)])
    while q:
        idx, node = q.popleft()
        l, r = min(l, idx), max(r, idx)
        d[idx].append(node.val)
        if node.left:
            q.append((idx-1, node.left))
        if node.right:
            q.append((idx+1, node.right))
    return [d[k] for k in range(l, r+1)]


#a modified level-order traversal
def verticalOrder2(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    
    q = []

    node = root
    q.append([node,0])
    
    output = {}

    while len(q) > 0:
        node,level = q.pop(0)
        
        if not (level in output):
            output[level] = [node.val]
        else:
            output[level].append(node.val)
        
        if node.left is not None:
            q.append([node.left,level-1])
        if node.right is not None:
            q.append([node.right,level+1])
    
    sortedkeys = sorted(output.keys())
    vertorder = []
    for i in sortedkeys:
        vertorder.append(output[i])
    return vertorder
