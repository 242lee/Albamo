from collections import deque 

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and board[ni][nj] == color:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    cnt += 1
    return cnt

M, N = map(int, input().split())
board = [list(input()) for _ in range(N)] 
visited = [[0] * M for _ in range(N)]

teamB = 0
teamW = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 'B':
            teamB += bfs(i, j, 'B') ** 2
        elif not visited[i][j] and board[i][j] == 'W':
            teamW += bfs(i, j, 'W') ** 2

print(teamW, teamB)
