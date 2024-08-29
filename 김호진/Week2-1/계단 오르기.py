# 백준 2579 계단 오르기 실3

import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

dp = [0] * n
dp[0] = arr[0]
if n >= 2:
    dp[1] = arr[1] + arr[0]
if n >= 3:
    dp[2] = arr[2] + max(arr[1], arr[0])
if n >= 4:
    for i in range(3, n):
        dp[i] = arr[i] + max(arr[i-1] + dp[i-3], dp[i-2])

print(dp[n-1])