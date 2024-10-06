# 백준 2447 별 찍기 - 10 골5
import sys
input = sys.stdin.readline

N = int(input())
arr = [['*'] * N for _ in range(N)]

k = 0
M = N // 3**(k+1)
while M:
    for x in range(M):
        a = 3**k + 3**(k+1) * x
        for y in range(M):
            b = 3**k + 3**(k+1) * y
            for i in range(a, a+3**k):
                for j in range(b, b+3**k):
                    arr[i][j] = ' '

    k += 1
    M = N // 3**(k+1)

for i in range(N):
    print(''.join(arr[i]))
