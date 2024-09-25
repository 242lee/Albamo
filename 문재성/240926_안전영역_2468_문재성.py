import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.read
data = list(map(int, input().split()))

N = data.pop(0)
rain = max(data)

# 2차원 배열로 변환
arr = []
for l in range(N):
    tmp = []
    for ll in range(N):
        tmp.append(data.pop(0))
    arr.append(tmp)

res = 0

# 비가 내리는 높이를 0부터 최고 높이까지 탐색
for rain_level in range(rain):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    # 배열의 각 칸을 순회하며 물에 잠기지 않은 구역 탐색
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain_level and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = 1

                # BFS 탐색
                while q:
                    vi, vj = q.popleft()
                    for ki, kj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = vi + ki, vj + kj
                        if 0 <= ni < N and 0 <= nj < N:
                            # 물에 잠기지 않은 지역이고, 아직 방문하지 않았으면 탐색
                            if arr[ni][nj] > rain_level and not visited[ni][nj]:
                                visited[ni][nj] = 1
                                q.append((ni, nj))

    # 최대 안전 구역 개수를 저장
    res = max(res, cnt)

print(res)
