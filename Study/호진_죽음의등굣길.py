# 백준 31946 죽음의 등굣길 실1

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    # 등굣길의 행의 개수 N(2~100)
M = int(input())    # 등굣길의 열의 개수 M(2~100)
# 보도블럭 (0 or 1)
arr = [list(map(int, input().split())) for _ in range(N)]

X = int(input())    # 점프력 X (1~10)

if arr[0][0] != arr[N-1][M-1]:
    print('DEAD')
    exit()


def check(i, j, ni, nj):
    if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
        if arr[i][j] == arr[ni][nj]:
            if ni == N-1 and nj == M-1:
                print('ALIVE')
                exit()
            dq.append([ni, nj])
            v[ni][nj] = 1


dq = deque([[0, 0]])
v = [[0] * M for _ in range(N)]
v[0][0] = 1
while dq:
    i, j = dq.popleft()
    for x in range(1, X+1):
        for d in range(0, x+1):
            check(i, j, i+d, j+(x-d))
            check(i, j, i-d, j+(x-d))
            check(i, j, i+d, j-(x-d))
            check(i, j, i-d, j-(x-d))

print('DEAD')
