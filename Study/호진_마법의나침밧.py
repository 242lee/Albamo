# 백준 32372 마법의 나침반 실4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 보물 후보 범위
x = y = 1

for _ in range(M):
    i, j, k = map(int, input().split())
    if k == 1 or k == 5:
        y = j
    if k == 3 or k == 7:
        x = i
    if k == 1 or k == 2 or k == 8:
        x = min(x, i+1)
    if k == 4 or k == 5 or k == 6:
        x = max(x, i+1)
    if k == 6 or k == 7 or k == 8:
        y = min(y, j+1)
    if k == 2 or k == 3 or k == 4:
        y = max(y, j+1)

print(x, y)