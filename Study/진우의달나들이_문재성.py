import sys
input = sys.stdin.readline

def dfs_search(n, m, dir, sum_v):
    global min_v

    if n == N-1:
        if min_v > sum_v:
            min_v = sum_v
        return

    if sum_v > min_v:
        return

    for d in range(3):
        if d != dir:
            nn, nm = n+dirs[d][0], m+dirs[d][1]
            if 0 <= nn < N and 0 <= nm < M:
                dfs_search(nn, nm, d, sum_v+arr[nn][nm])

N, M = map(int, input().split())
dirs = ((1, -1), (1, 0), (1, 1))
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = int(1e9)

for j in range(M):
    i = 0
    for k in range(3):
        dfs_search(i, j, k, arr[i][j])

print(min_v)
