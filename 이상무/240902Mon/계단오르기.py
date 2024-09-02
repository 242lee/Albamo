import sys
n = int(input())
s = [int(sys.stdin.readline()) for _ in range(n)]

dp = []
# 이 문제는 3개의 계단을 연속으로 한 칸씩 가지 못한다.
# 그러므로 1, 2번째 칸은 그냥 규칙없이 그 전 칸의 합이 그 칸의 최대값이다.
# 3번째 칸부터는 총 2가지 경우로 그 층의 도달할 수 있다. 첫 번재는 그 전 칸에서 한 칸 올라가는 경우, 두 번째는 그 전전 칸에서 두 칸 올라가는 경우이다.

for i in range(2):
  dp.append(sum(s[:i + 1])) 
if n >= 3:
  dp.append(max(s[0] + s[2], s[1] + s[2]))
for i in range(3, n):
  dp.append(max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i]))   # 좌측은 1칸 올라왔을 경우, 우측은 2칸 올라왔을 경우.
answer = dp.pop()

print(answer)

