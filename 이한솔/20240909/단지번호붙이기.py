'''
한솔의 BFS 재활2

수정중

상하좌우
단지수 출력
단지 별 집의 수 오름차순 출력
'''

from collections import deque


n = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

arr = [list(map(int, input())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
apart = []

def bfs(arr,l,k):
    q = deque()
    q.append((l,k))
    arr[l][k] = 0
    visited[l][k] = 1
    cnt = 1

    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            apart.append(bfs(arr,i,j))

apart.sort()
print(len(apart))
for i in apart:
    print(i)