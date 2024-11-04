# dfs or bfs를 써야하는 문제.
# 1에서 bfs를 사용해서 not visited인 곳을 다니면서 +1씩 해주고, 가장 큰 값을 가진 수의 개수를 세면 된다.

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    # BFS 탐색
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    max_distance = max(distances)
    return distances.count(max_distance)
