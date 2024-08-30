'''
게단은 한 칸 또는 두 칸씩 
연속 세 개 안됨
시작점은 포함 안함
마지막 계단은 꼭 밟아야함
'''

n = int(input())
dp = [0]*n
arr = [int(input()) for _ in range(n)]                                                                                                      

# 계단이 2칸 이하일 경우는 둘 다 더한 것이 최대
# 2칸 이하와 3칸 이상일 경우를 나눠

if n <= 2:
    print(sum(arr))
else: # 3칸 이상일 경우
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
        # i-1, i번째 계단을 연속으로 밟기 때문에 그 전의 계단은 i-3
    print(dp[-1])

