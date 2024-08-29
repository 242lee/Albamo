# 백준 7568 덩치 실5

from sys import stdin
input = stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

rank = [0] * n
for i in range(n):
    cnt = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    rank[i] = cnt

print(*rank)