# 소프티어 스마트 물류 Lv3
import sys
input = sys.stdin.readline

# 1 <= N <= 20000, 1 <= K <= 10
N, K = map(int, input().split())
arr = list(map(str, input().strip()))

'''
풀이 아이디어
양쪽 끝 바깥에서부터 부품을 집어나가면 최대로 부품을 집게 됨
'''

ans = 0
# 왼쪽부터 절반 탐색
for i in range(N//2):
    # 로봇이면 왼쪽 K 범위부터 부품 찾으면 집기
    if arr[i] == 'P':
        for j in range(-K, K+1):
            if 0 <= i+j < N and arr[i+j] == 'H':
                ans += 1
                arr[i+j] = 'X'
                break

# 오른쪽 절반 탐색
for i in range(N-1, N//2-1, -1):
    # 로봇이면 오른쪽 K 범위부터 부품 찾으면 집기
    if arr[i] == 'P':
        for j in range(K, -K-1, -1):
            if 0 <= i+j < N and arr[i+j] == 'H':
                ans += 1
                arr[i+j] = 'X'
                break

print(ans)
