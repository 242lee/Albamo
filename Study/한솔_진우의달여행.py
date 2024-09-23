'''
아래 방향으로만 이동할 수 있음
같은 방향으로 두 번 가지 못하도록 어케 하지?
가장 위의 줄 4군데서 출발하는 모든 경우의 수?
DP 만들고 가장 아래 줄 중에서 가장 낮은 수 뽑기?
'''

n, m = map(int, input().split())
fuels = [list(map(int, input().split())) for _ in range(n)]
# 연료 정보를 담아

# 최소값을 저장하기 위한 3차원 리스트 생성
# 가장 작은 값을 찾아야하므로 가장 큰 값으로 초기화 
dp = [[[int(1e9)]*3 for _ in range(m)] for _ in range(n+1)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = 0

# 첫번째 행의 모든 열에서 출발할 수 있고 아직 연료를 쓰지 않으므로 0으로 초기화
# dp[i][j][k] 에서 i는 행, j는 열, k는 이전에 어떤 방향으로 움직였는지 저장할거야
# k 가 0이면 왼쪽에서 이동한 것, 1이면 위에서 이동한 것, 2이면 오른쪽에서 이동한 것
 
for i in range(1, n+1):
    for j in range(m):
        # 왼쪽 끝이면 위, 오른쪽만 가능
        if j==0:
            dp[i][j][1] = dp[i-1][j][2]+fuels[i-1][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1])+fuels[i-1][j]
        # 중간이면 세방향 모두 가능
        elif 0<j<m-1:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2])+fuels[i-1][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2])+fuels[i-1][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1])+fuels[i-1][j]
        # 오른쪽 끝이면 위, 왼쪽만 가능
        else:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2])+fuels[i-1][j]
            dp[i][j][1] = dp[i-1][j][0]+fuels[i-1][j]

ans = int(1e9)

# 마지막 행에서 가장 작은 값이 정답
for j in range(m):
    ans = min(min(dp[n][j]), ans)

print(ans)


