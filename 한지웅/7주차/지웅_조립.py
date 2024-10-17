# 20000 N
# 1 ~ 10 K
import sys
from copy import deepcopy

sys.setrecursionlimit(10**9)

N, K = map(int,input().split())
matrix = list(input())
matrixIndexInfo = []
matrixIndex = 0
for i in range(N):
    if matrix[i] == 'P':
        matrixIndexInfo.append(i)
mx = 0

def dfs(currentIndex, numb, matr):
    global mx, matrixIndex
    if matrixIndex >= len(matrixIndexInfo):
        if mx < numb:
            mx = numb
        return
    current = matrixIndexInfo[currentIndex]
    matrixIndex += 1
    if N - current < mx - numb:
        return
    for dist in range(-K, K+1):
        next = current + dist
        if 0<= next < N and matrix[next] == 'H':
            nxt_matr = deepcopy(matr)
            nxt_matr.add(next)
            if len(nxt_matr) != len(matr):
                dfs(matrixIndex, numb + 1, nxt_matr)
    dfs(matrixIndex, numb, matr)

dfs(0, 0, set())
print(mx)
