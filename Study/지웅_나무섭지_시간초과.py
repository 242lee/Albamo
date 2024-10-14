from collections import deque

n, m = map(int,input().split())
matrix = []
exit = None
start = None
walls = []
ghosts = []

dirInfo = [(0,1),(0,-1), (1,0), (-1,0)]

for iIndex in range(n):
    oneLine = input()
    matrix.append(list(oneLine))
    for jIndex in range(m):
        if oneLine[jIndex] == 'D':
            exit = (iIndex, jIndex)
        elif oneLine[jIndex] == 'N':
            start = (iIndex, jIndex)
        elif oneLine[jIndex] == 'G':
            ghosts.append((iIndex, jIndex))
        elif oneLine[jIndex] == '#':
            walls.append((iIndex, jIndex))
        else:
            continue

def checkValid(i, j, step):
    if 0 > i or n <= i or m <= j or 0 > j:
        return False
    if matrix[i][j] == '#':
        return False
    for ghostNumber in range(len(ghosts)):
        ghostI = ghosts[ghostNumber][0]
        ghostJ = ghosts[ghostNumber][1]
        if ghostI - step <= i <= ghostI + step and ghostJ - step <= j <= ghostJ + step:
            return False
    return True

def bfs():
    QI = deque()
    QJ = deque()
    STEP = deque()
    QI.append(start[0])
    QJ.append(start[1])
    STEP.append(0)
    while QI:
        nowI = QI.popleft()
        nowJ = QJ.popleft()
        nowStep = STEP.popleft()
        for dir in range(4):
            nextI = nowI + dirInfo[dir][0]
            nextJ = nowJ + dirInfo[dir][1]
            if checkValid(nextI, nextJ, nowStep) == True:
                if (nextI, nextJ) == exit:
                    return True
                QI.append(nextI)
                QJ.append(nextJ)
                STEP.append(nowStep + 1)
                matrix[nextI][nextJ] = 'N'
    return False


result = bfs()
if result == True:
    print('Yes')
else:
    print('No')
