# 백준 8979 올림픽 실5

import sys
input = sys.stdin.readline

N, k = map(int, input().split())
country = [0] * N
for _ in range(N):
    n, g, s, b = map(int, input().split())
    country[n-1] = [g, s, b, n]

country.sort(reverse=True)
for i in range(N):
    if country[i][3] == k:
        j = i
        while country[j-1][:3] == country[i][:3]:
            j -= 1
        print(j + 1)
        break
