'''
한솔의 BFS 재활1

(1,1) 출발 , (N,M) 도착
최소 칸
인접한 칸만 이동 가능
'''

from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

q = deque()
visited = [[1]*m for _ in range(n)]

q.append((0,0))
visited[0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 1 and arr[nx][ny] == 1:
            q.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][m-1])



