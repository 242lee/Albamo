# 전위 순회: 루트 → 왼쪽 자식 → 오른쪽 자식
# 후위 순회: 왼쪽 자식 → 오른쪽 자식 → 루트

import sys
sys.setrecursionlimit(10**6)

def build_tree(nodes):
    if not nodes:
        return None
    
    # 현재 루트 노드 선택 (y가 가장 크고, x가 가장 작은 노드)
    x, y, idx = nodes[0]
    root = {"idx": idx, "left": None, "right": None}
    
    # x 값 기준으로 왼쪽, 오른쪽 서브트리 구분
    left_nodes = [node for node in nodes if node[0] < x]
    right_nodes = [node for node in nodes if node[0] > x]
    
    # 재귀적으로 왼쪽과 오른쪽 서브트리 생성
    root["left"] = build_tree(left_nodes)
    root["right"] = build_tree(right_nodes)
    
    return root

def preorder(node, result):
    if node is None:
        return
    result.append(node["idx"])  # 현재 노드 방문
    preorder(node["left"], result)
    preorder(node["right"], result)

def postorder(node, result):
    if node is None:
        return
    postorder(node["left"], result)
    postorder(node["right"], result)
    result.append(node["idx"])  # 현재 노드 방문

def solution(nodeinfo):
    # 노드 정보에 인덱스 추가
    nodes = [(x, y, idx + 1) for idx, (x, y) in enumerate(nodeinfo)]
    # y 기준 내림차순, x 기준 오름차순으로 정렬
    nodes.sort(key=lambda x: (-x[1], x[0]))

    # 트리 구성
    root = build_tree(nodes)

    # 전위 순회와 후위 순회 결과 구하기
    pre_result, post_result = [], []
    preorder(root, pre_result)
    postorder(root, post_result)

    return [pre_result, post_result]
