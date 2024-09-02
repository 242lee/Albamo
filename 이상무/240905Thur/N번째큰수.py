import sys, bisect
from collections import deque

input = sys.stdin.readline
n = int(input())

ans = deque([-10**8] * n)
for _ in range(n):
    for i in list(map(int, input().strip().split())):
        bisect.insort(ans, i)
        ans.popleft()
print(ans[0])
