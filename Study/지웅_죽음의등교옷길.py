from collections import deque as DQ
def bfs():
    CI = 0
    CJ = 0
    color = matrix[0][0]
    DQI = DQ()
    DQJ = DQ()
    matrix[0][0] = 2
    while True:
        for i in range(-X,X+1):
            for j in range(-X,X+1):
                if abs(i) + abs(j) <= X and (i == 0 and j == 0) == False:
                    NI = CI + i
                    NJ = CJ + j
                    if 0<= NI < N and 0<= NJ < M and matrix[NI][NJ] == color:
                        matrix[NI][NJ] = 2
                        DQI.append(NI)
                        DQJ.append(NJ)
        # print(DQI, DQJ)
        if DQI == DQ():
            return matrix[N-1][M-1]
        CI = DQI.popleft()
        CJ = DQJ.popleft()
N = int(input())
M = int(input())
matrix = [];
for _ in range(N):
    matrix.append(list(map(int,input().split())))
X = int(input())
result = bfs()
if result != 2:
    print('DEAD')
else:
    print('ALIVE')
