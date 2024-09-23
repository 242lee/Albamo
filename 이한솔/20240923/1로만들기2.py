'''
완벽히 이해 못함 설명해줘 이상무무
'''

n = int(input())

dp = [0]*1000001

# dp[1]은 이미 1이므로 2부터 순회
for i in range(2, n+1):
    # 1을 빼기
    dp[i] = dp[i-1] + 1                      
    # 2로 나누기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

result = [n]
now = n
temp = dp[n] - 1

# n 부터 하나씩 줄여나가면서 순서 찾기
for i in range(n, 0, -1):
    if dp[i] == temp and (i + 1 == now or i*2 == now or i*3 == now):
        now = i
        result.append(i)
        temp -= 1

print(*result)