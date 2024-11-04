# 간선 양방향
# 20000개의 노드와 50000개의 간선

from collections import deque

def makeMatrix(n,lst):
    matrix = [[] for _ in range(n+1)]
    for i in range(len(lst)):
        node1, node2 = lst[i]
        matrix[node1].append(node2)
        matrix[node2].append(node1)
    return matrix

def bfs(n, edge):
    visited = [0 for _ in range(n+1)]
    matrix = makeMatrix(n, edge)
    mx_distance = 0
    mx_nodes = set()
    q = deque([1])
    visited[1] = 1
    while q:
        current = q.popleft()
        for i in range(len(matrix[current])):
            nextCandidate = matrix[current][i]
            if visited[nextCandidate] == 0:
                visited[nextCandidate] = visited[current] + 1
                q.append(nextCandidate)
                if mx_distance < visited[current] + 1:
                    mx_distance = visited[current] + 1
                    mx_nodes = set()
                    mx_nodes.add(nextCandidate)
                else:
                    mx_nodes.add(nextCandidate)
    return mx_nodes
    
def solution(n, edge):
    answer = 0
    result = bfs(n,edge)
    answer = len(result)
    return answer
