import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

white, blue = 0, 0

for i in range(M):
    for j in range(N):
        first = arr[i][j]
        if not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            cnt = 0
            while q:
                cx, cy = q.popleft()
                cnt += 1
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == first:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            power = cnt ** 2
            if first == 'W':
                white += power
            else:
                blue += power

print(white, blue)
