# 백준 16918 봄버맨 실버1
from collections import deque
import sys
input = sys.stdin.readline

# 1 ~ 200
R, C, N = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]

dq = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            arr[i][j] = 0
            dq.append([i, j, 0])

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

for sec in range(2, N+1):
    # 짝수 초에는 폭탄 추가
    if sec % 2 == 0:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == '.':
                    arr[i][j] = sec
                    dq.append([i, j, sec])
    
    # 홀수 초에는 KA-BOOM
    else:
        while dq and dq[0][2] == sec - 3:
            # 심어둔 폭탄 터트릴 준비
            i, j, t = dq.popleft()
            # 실제로 심어져 있으면 KA-BOOM
            if arr[i][j] == sec - 3:
                arr[i][j] = '.'
                # 사방 폭탄 파괴
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    # 이번에 터트려야할 폭탄이 아니면 파괴
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != '.' and arr[ni][nj] != sec - 3 :
                        arr[ni][nj] = '.'

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            print('.', end='')
        else:
            print('O', end='')
    print()