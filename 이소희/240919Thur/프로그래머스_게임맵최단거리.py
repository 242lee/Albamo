from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def bfs(i, j):
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = [[0] * m for _ in range(n)]
        visited[i][j] = 1
        
        q = deque()
        q.append((i, j))
        
        while q:
            ci, cj = q.popleft()
            for di, dj in dir:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and  maps[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    
                    if ni == n-1 and nj == m-1:
                        return visited[ni][nj]
        return -1

    return bfs(0,0)