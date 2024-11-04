import sys
sys.setrecursionlimit(10000)

# Node 클래스 정의
class Node:
    def __init__(self, x, y, idx):
        # 각 노드의 x 좌표, y 좌표, 노드 번호를 초기화
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

# 부모 노드에 자식 노드를 삽입하는 함수
def insert_node(parent, child):
    # 자식 노드의 x 값이 부모 노드의 x 값보다 작으면 왼쪽에 삽입
    if child.x < parent.x:
        if parent.left is None:  # 왼쪽 자식 노드가 비어있으면
            parent.left = child
        else:  # 이미 왼쪽 자식 노드가 있으면 재귀적으로 삽입
            insert_node(parent.left, child)
    else:
        # 자식 노드의 x 값이 부모 노드의 x 값보다 크면 오른쪽에 삽입
        if parent.right is None:  # 오른쪽 자식 노드가 비어있으면
            parent.right = child
        else:  # 이미 오른쪽 자식 노드가 있으면 재귀적으로 삽입
            insert_node(parent.right, child)

# 전위 순회(preorder traversal) 함수
def preorder_traversal(node, traversal):
    if node is not None:
        traversal.append(node.idx)  # 현재 노드를 먼저 방문
        preorder_traversal(node.left, traversal)  # 왼쪽 서브트리를 순회
        preorder_traversal(node.right, traversal)  # 오른쪽 서브트리를 순회

# 후위 순회(postorder traversal) 함수
def postorder_traversal(node, traversal):
    if node is not None:
        postorder_traversal(node.left, traversal)  # 왼쪽 서브트리를 순회
        postorder_traversal(node.right, traversal)  # 오른쪽 서브트리를 순회
        traversal.append(node.idx)  # 현재 노드를 마지막에 방문

# 주어진 nodeinfo를 기반으로 트리를 구성하고 순회 결과를 반환하는 함수
def solution(nodeinfo):
    # Node 객체 리스트 생성, 각 노드는 x, y 좌표와 인덱스를 가짐
    nodes = [Node(x, y, idx+1) for idx, (x, y) in enumerate(nodeinfo)]
    # 노드를 y 좌표 내림차순, x 좌표 오름차순으로 정렬
    nodes.sort(key=lambda n: (-n.y, n.x))
    
    # 첫 번째 노드를 루트로 설정
    root = nodes[0]
    # 나머지 노드들을 트리에 삽입
    for node in nodes[1:]:
        insert_node(root, node)
    
    # 전위 순회와 후위 순회를 저장할 리스트 초기화
    preorder_result = []
    postorder_result = []
    
    # 전위 순회와 후위 순회 실행
    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)
    
    # 두 순회 결과를 반환
    return [preorder_result, postorder_result]
