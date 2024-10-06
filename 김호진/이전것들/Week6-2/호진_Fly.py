# 백준 1011 Fly me to the Alpha Centauri 골5
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    R = Y - X
    n = 1
    s = n*(n+1) // 2
    while s < R // 2:
        n += 1
        s = n*(n+1) // 2

    if s*2 - n > R:
        n -= 1
        s = n*(n+1) // 2

    if R - s*2 > n+1:
        print(n*2 + 2)
    elif 0 < R - s*2 <= n+1:
        print(n*2 + 1)
    elif -n < R - s*2 <= 0:
        print(n*2)
    elif R - s*2 == -n:
        print(n*2 - 1)
