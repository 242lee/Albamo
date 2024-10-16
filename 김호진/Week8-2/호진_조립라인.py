# 소프티어 조립라인 Lv3
import sys
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input())

# 각 작업시간 및 이동시간 입력받기
A = [0] * N
B = [0] * N
A_to_B = [0] * (N-1)
B_to_A = [0] * (N-1)

for i in range(N-1):
    A[i], B[i], A_to_B[i], B_to_A[i] = map(int, input().split())
A[-1], B[-1] = map(int, input().split())

'''
N의 범위가 1000까지이므로 이론상 2^1000승 개의 경우의 수가 생긴다.
즉, dp 아니면 greedy 인데, 1부터 1000까지 최적의 값을 찾아나간다는 느낌으로
dp를 선택함. greedy를 하기엔 최소시간을 찾는 특정한 규칙성을 발견하지 못한다.

dp를 이제 어떻게 써야할까 생각해보면,
k번째에 A를 선택하는 최소시간은 아래 둘 중의 최소값이다. (B도 마찬가지)
    지난 A 최소시간 + 이번 A 작업시간
    지난 B 최소시간 + 저번 B -> 이번 A 이동시간 + 이번 A 작업시간
그리고 마지막 A와 B를 선택하는 최소시간 중 최소값이 정답이다.
'''
dp = [[0, 0] for _ in range(N)]

dp[0][0] = A[0]
dp[0][1] = B[0]

if N >= 2:
    for i in range(1, N):
        dp[i][0] = min(
            dp[i-1][0] + A[i],
            dp[i-1][1] + B_to_A[i-1] + A[i]
        )
        dp[i][1] = min(
            dp[i-1][1] + B[i],
            dp[i-1][0] + A_to_B[i-1] + B[i]
        )

print(min(dp[N-1][0], dp[N-1][1]))
