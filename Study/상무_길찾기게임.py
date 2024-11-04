# 전위순회
# [x, y]값으로 input 받음
# 1. x축 y축 기준으로 정렬하는게 의미가 있을까?
# 별로 없을 것 같다.

# 2. 가장 y가 높은 노드 = root (append)
# root보다 x가 낮고 y가 가장 높은 노드 = node_now => 왼쪽 tree (append)
# if node_now보다 x가 낮은 노드가 없으면 .. 

import sys; sys.setrecursionlimit(10001)

def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    # [(1, 5, 3), (2, 11, 5), (3, 13, 3), (4, 3, 5), (5, 6, 1), (6, 1, 3), (7, 8, 6), (8, 7, 2), (9, 2, 2)]
    return traversal(nodes, [], [])

def traversal(nodes, pre, post):
    # y가 가장 높은 노드를 반환
    parent, x, y = sorted(nodes, key=lambda x: x[2])[-1]
    # nodes들 중 x값을 비교해서 작으면 왼쪽, 크면 오른쪽
    left = [node for node in nodes if node[1] < x]
    right = [node for node in nodes if node[1] > x]
    # 전위순회는 여기서 부모노드를 append 해준다.
    pre.append(parent)
    
    # 왼쪽 서브트리를 순회
    if left: 
        pre, post = traversal(left, pre, post)
    
    # 만약 중위순회가 있었으면 여기서 append를 해준다.

    # 오른쪽 서브트리를 순회
    if right: 
        pre, post = traversal(right, pre, post)
    
    # 후위 순회는 여기서 노드를 append 해준다.
    post.append(parent)
    return pre, post

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))