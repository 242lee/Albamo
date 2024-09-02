# 계단 오르기

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

dp = [0] * N
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

dp[0] = stairs[0]

if N >= 2 :
    dp[1] = stairs[0] + stairs[1]
if N >= 3:
    dp[2] = stairs[2] + max(stairs[1], stairs[0])
if N >= 4:
    for i in range(3, N):
        dp[i] = stairs[i] + max(stairs[i-1] + dp[i-3], dp[i-2])


print(dp[N-1])

