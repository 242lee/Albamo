'''
Ai 작업장의 작업시간, Bi 작업장의 작업시간, Ai 작업장에서 Bi+1 작업장까지 이동시간, Bi 작업장에서 Ai+1 작업장까지 이동시간

Ai + 1 번째의 최소 시간
= min (Ai 일 때 최소 시간 + Ai+1 일 때 시간, Bi일 때 최소 시간 + BtoA 이동시간 + Ai+1 일 때 시간)
Bi+1 번 째의 최소 시간
= min (Ai일 때 최소 시간 + AtoB 이동시간 + Bi+1 일 때 시간, Bi 일 때 최소 시간 + Bi+1 일 때 시간)
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
hours = []

for i in range(N):
    hours.append(list(map(int, input().split())))

# dp 배열을 초기화
dp = [[0, 0] for _ in range(N)]

# 첫 번째 작업장 초기화
dp[0] = [hours[0][0], hours[0][1]]

for i in range(1, N):
    # A 라인의 i번째 작업장까지의 최소 시간
    dp[i][0] = min(dp[i-1][0] + hours[i][0], dp[i-1][1] + hours[i-1][3] + hours[i][0])
    # B 라인의 i번째 작업장까지의 최소 시간
    dp[i][1] = min(dp[i-1][1] + hours[i][1], dp[i-1][0] + hours[i-1][2] + hours[i][1])

print(min(dp[N-1]))
