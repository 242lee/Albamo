# 처음 시작 점에서 그 다음 점까지 진행.
# 합만 구하면 방향성을 제어를 못한다.
# 합과 동시에 왼쪽으로 진행하는지, 아래로 진행하는지, 오른쪽으로 진행하는지 방향성 제시
# 맨 오른쪽에서 시작해서 왼쪽으로만 진행해도 달에 도착할 수 있다. 이 점을 노릴 수 있을까 (노리지 못함)
# 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
    	# 바로 위, 오른쪽 위에 값만 비교(왼쪽 위의 값 없음)
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + matrix[i-1][j]
        # 바로 위, 왼쪽 위에 값만 비교(오른쪽 위의 값 없음)
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + matrix[i-1][j]
        # 전체 값 비교 가능
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + matrix[i-1][j]

min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)
print(min_value)