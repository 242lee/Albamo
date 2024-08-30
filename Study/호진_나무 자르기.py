# 백준 2805 나무 자르기 실2

import sys
input = sys.stdin.readline

# 나무 수 n (1 ~ 1,000,000), 가져갈 나무 길이 m (1 ~ 2,000,000,000)
n, m = map(int, input().split())
# 나무 n개의 길이 (1 ~ 1,000,000,000)
trees = list(map(int, input().split()))
trees.sort(reverse=True)

ss = 0

if n == 1:
    ss = trees[0]
    h = 0
    w = 1
else:
    for i in range(1, n):
        ss += (trees[i-1] - trees[i]) * i
        if ss >= m:
            h = trees[i]
            w = i
            break
    else:
        ss += trees[i] * n
        h = 0
        w = n

if ss > m:
    h += (ss - m) // w

print(h)