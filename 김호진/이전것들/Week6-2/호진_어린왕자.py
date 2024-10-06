# 백준 1004 어린 왕자 실3
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    ans = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        flag = 0
        if (x1-cx)**2 + (y1-cy)**2 < r**2:
            ans += 1
            flag = 1
        if (x2-cx)**2 + (y2-cy)**2 < r**2:
            if flag == 1:
                ans -= 1
            else:
                ans += 1

    print(ans)
