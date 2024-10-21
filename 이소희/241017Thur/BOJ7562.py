from collections import deque
directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]    

def bfs(si, sj, ei, ej):
    q = deque([(si, sj)]) 
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return visited[ci][cj] - 1
        for dir in directions:
            ni, nj = ci + dir[0], cj + dir[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))

TC = int(input())
for _ in range(TC):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    print(bfs(si, sj, ei, ej))
    

