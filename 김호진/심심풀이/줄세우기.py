# 백준 10431 줄세우기 실5
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    case, *arr = list(map(int, input().split()))
    ans = 0
    for i in range(20):
        for j in range(0, i):
            if arr[j] > arr[i]:
                ans += 1

    print(case, ans)