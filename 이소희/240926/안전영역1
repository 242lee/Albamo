'''
656ms
'''
N = int(input())
road = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, h, visited):
    stack = [(i, j)]
    visited[i][j] = 1

    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and road[ni][nj] > h:
                visited[ni][nj] = 1
                stack.append((ni, nj))

maxSafeZone = 0
maxHeight = max(map(max, road))

for h in range(maxHeight + 1): 
    visited = [[0] * N for _ in range(N)]
    safe_zones = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] > h and not visited[i][j]:
                dfs(i, j, h, visited)
                safe_zones += 1
    maxSafeZone = max(maxSafeZone, safe_zones)

print(maxSafeZone)
