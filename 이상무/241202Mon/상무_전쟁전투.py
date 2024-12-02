import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
battleground = [list(input().strip()) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, col):
    q = deque()
    q.append((x,y))
    cnt = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <=ny < N:
                if battleground[nx][ny] == col and battleground[nx][ny] != 0:
                    q.append((nx,ny))
                    cnt += 1
                    battleground[nx][ny] = 0
    
    if cnt == 0:
        return 1
    else:
        return cnt


w_cnt, b_cnt = 0, 0

for i in range(M):
    for j in range(N):
        if battleground[i][j] != 0:
            if battleground[i][j] == 'W':
                w_cnt += bfs(i, j, battleground[i][j])**2
            elif battleground[i][j] == 'B':
                b_cnt += bfs(i, j, battleground[i][j])**2
            
print(w_cnt, b_cnt)