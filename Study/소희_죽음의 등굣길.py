from collections import deque

N = int(input())
M = int(input())
road = [list(map(int, input().split())) for _ in range(N)]
X = int(input())

# (0, 0) -> (N-1, M-1)
# 시작점과 목표점의 색이 다르면 DEAD 
if road[0][0] != road[N-1][M-1]:
    print("DEAD")
    exit()

# BFS로 최단 경로 탐색
def bfs():
    queue = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    color = road[0][0]
    while queue:
        i, j = queue.popleft()

        if i == N-1 and j == M-1:
            return "ALIVE"

        # 맨해튼 거리 내에 있는 좌표 탐색
        for ni in range(max(0, i-X), min(N, i+X+1)):
            for nj in range(max(0, j-X), min(M, j+X+1)):
                if abs(ni - i) + abs(nj - j) <= X:
                    if not visited[ni][nj] and road[ni][nj] == color:
                        visited[ni][nj] = 1
                        queue.append((ni, nj))
    return "DEAD"

print(bfs())
