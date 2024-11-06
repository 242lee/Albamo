import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

def add_node(parent, child):
    if parent.x > child.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

def preorder(node, result):
    if node is None:
        return
    result.append(node.idx)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.idx)

def solution(nodeinfo):
    nodes = [(x, y, idx + 1) for idx, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    root = TreeNode(*nodes[0])
    for x, y, idx in nodes[1:]:
        add_node(root, TreeNode(x, y, idx))
    
    pre_result = []
    post_result = []
    preorder(root, pre_result)
    postorder(root, post_result)
    
    return [pre_result, post_result]


# return [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))