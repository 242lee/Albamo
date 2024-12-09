# 백준 1303 전쟁 - 전투 실버1
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

dq = deque()
v = [[0] * M for _ in range(N)]
ans_w = ans_b = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            v[i][j] = 1
            if arr[i][j] == 'W':
                now = 'W'
            else:
                now = 'B'
            dq.append([i, j])
            cnt = 1
            while dq:
                x, y = dq.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == now:
                        dq.append([nx, ny])
                        v[nx][ny] = 1
                        cnt += 1
            if now == 'W':
                ans_w += cnt**2
            else:
                ans_b += cnt**2

print(ans_w, ans_b)