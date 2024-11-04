from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distances = [-1] * (n + 1)
    distances[1] = 0                    # 노드의 시작
    q = deque([1])
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distances[next] == -1 :  # 아직 방문 전인 노드
                distances[next] = distances[now] + 1
                q.append(next)
    max_d = max(distances)
    return distances.count(max_d)
    
    return graph