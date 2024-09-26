'''
668ms
'''
from collections import deque

N = int(input())
road = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, h, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        for i in range(4):
            ni, nj = i + di[i], j + dj[i]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and road[ni][nj] > h:
                visited[ni][nj] = True
                queue.append((ni, nj))

maxSafeZone = 0
maxHeight = max(map(max, road)) 

for h in range(maxHeight + 1): 
    visited = [[False] * N for _ in range(N)]
    safe_zones = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                safe_zones += 1
    maxSafeZone = max(maxSafeZone, safe_zones)

print(maxSafeZone)
