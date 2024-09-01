"""
6
10
20
15
25
10
20
"""

n = int(input())  # 계단의 개수 입력
stairs = [int(input()) for _ in range(n)]  # 각 계단의 점수 입력

# DP 테이블 초기화
dp = [0] * n

# 초기값 설정
dp[0] = stairs[0]  # 첫 번째 계단의 최대 점수는 그 계단의 점수와 동일
if n > 1:
    dp[1] = stairs[0] + stairs[1]  # 두 번째 계단은 첫 번째와 두 번째 계단 점수의 합
if n > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])  # 세 번째 계단은 첫 번째 + 세 번째 또는 두 번째 + 세 번째 중 큰 값

# DP 점화식을 사용하여 최대 점수 계산
for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# 마지막 계단까지의 최대 점수 출력
print(dp[-1])

