# 백준 2468 안전 영역 실1
from collections import deque
import sys
input = sys.stdin.readline


def count_safe(height):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > height and v[i][j] == 0:
                cnt += 1
                bfs(i, j, height)
    return cnt


def bfs(i, j, h):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    dq = deque([[i, j]])
    v[i][j] = 1
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h and v[nx][ny] == 0:
                dq.append([nx, ny])
                v[nx][ny] = 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

bit = [0] * 101
ans = 1
for i in range(n):
    for j in range(n):
        if bit[arr[i][j]] == 0:
            v = [[0] * n for _ in range(n)]
            ans = max(ans, count_safe(arr[i][j] - 1))
            bit[arr[i][j]] = 1

print(ans)
