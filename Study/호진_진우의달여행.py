# 백준 17484 진우의 달 여행 실3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j, ss):
    global ans
    
    if i == N-1:
        ans = min(ans, ss)
        return

    if ans <= ss:
        return

    if 0 <= j-1 and not(0 <= i-1 and j+1 < M and v[i-1][j+1] == 1):
        v[i+1][j-1] = 1
        dfs(i+1, j-1, ss+arr[i+1][j-1])
        v[i+1][j-1] = 0

    if not(0 <= i-1 and v[i-1][j] == 1):
        v[i+1][j] = 1
        dfs(i+1, j, ss+arr[i+1][j])
        v[i+1][j] = 0

    if j+1 < M and not(0 <= i-1 and 0 <= j-1 and v[i-1][j-1] == 1):
        v[i+1][j+1] = 1
        dfs(i+1, j+1, ss+arr[i+1][j+1])
        v[i+1][j+1] = 0


ans = 600
for j in range(M):
    v = [[0] * M for _ in range(N)]
    v[0][j] = 1
    dfs(0, j, arr[0][j])

print(ans)