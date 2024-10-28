from copy import deepcopy
from collections import deque

di = [0,1,-1,0,1,-1,1,-1]
dj = [1,0,0,-1,1,1,-1,-1]

layer_one = list(input())
layer_two = list(input())
layer_three = list(input())
layer_four = list(input())
matrix = [layer_one, layer_two, layer_three, layer_four]
visited = [[0 for _ in range(10)] for l in range(4)]
pivot_one = deepcopy(layer_one)
pivot_two = deepcopy(layer_two)
pivot_three = deepcopy(layer_three)
pivot_four = deepcopy(layer_four)
pivot = list(input())
mx_idx = (0,0)
mn_idx = (3,9)
mid_idx = (0,0)

def bfs(i,j):
    global mx_idx, mn_idx, mid_idx
    Qi = deque()
    Qj = deque()
    Qi.append(i)
    Qj.append(j)
    visited[i][j] = 1
    while True:
        nowI = Qi.popleft()
        nowJ = Qj.popleft()
        doubleValue = nowI**2 + nowJ**2
        if doubleValue > mx_idx[0]**2 + mx_idx[1]**2:
            mx_idx = (nowI,nowJ)
        if doubleValue < mn_idx[0]**2 + mn_idx[1]**2:
            mn_idx = (nowI,nowJ)
        if mx_idx[0] - mn_idx[0] == 2 and mx_idx[1] - mn_idx[1] == 2:
            mid_idx = (int((mx_idx[0] + mn_idx[0]) / 2), int((mx_idx[1] + mn_idx[1]) / 2))
            return
        # print(matrix[nowI][nowJ])
        for dir in range(8):
             nextI = nowI + di[dir]
             nextJ = nowJ + dj[dir]
             if 0<=nextI<4 and 0<=nextJ<10 and matrix[nextI][nextJ] in pivot and visited[nextI][nextJ] == 0:
                 visited[nextI][nextJ] = 1
                 Qi.append(nextI)
                 Qj.append(nextJ)
                 break
        else:
            if len(Qi) == 0:
                return

def checkKeyBoard():
    for i in range(4):
        for j in range(10):
            if matrix[i][j] in pivot:
                bfs(i,j)
                return

checkKeyBoard()

# print(mid_idx)
print(matrix[mid_idx[0]][mid_idx[1]])
