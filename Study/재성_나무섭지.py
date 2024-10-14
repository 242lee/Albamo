import sys
from collections import deque
input = sys.stdin.readline

'''
유령이 움직일 경로는 계산할 필요없고 
유령은 벽 상관없이 이동 가능하기 때문에
출구에 남우보다 빨리 도달할 수 있다면 
남우를 막을 수 있다고 생각하면 댐
그래서 그냥 맨해튼 거리로 최단거리를 구할 수 있음
'''

n, m = map(int, input().split())
ghosts = []
goal = None
arr = []
start = None

# 입력 파싱 및 초기화
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'G':
            ghosts.append((i, j))
            tmp[j] = 0
        elif tmp[j] == 'D':
            goal = (i, j)
            tmp[j] = 0
        elif tmp[j] == '.':
            tmp[j] = 0
        elif tmp[j] == '#':
            tmp[j] = 1
        elif tmp[j] == 'N':
            start = (i, j)
            tmp[j] = 0
    arr.append(tmp)

# 유령이 있는 경우: 유령과 출구의 맨해튼 거리 최솟값 계산
min_ghost_dist = min(abs(gx - goal[0]) + abs(gy - goal[1]) for gx, gy in ghosts) if ghosts else None

# 남우 BFS (유령이 있는 경우와 없는 경우 모두 처리)
q = deque([start])
visited = [[float('inf')] * m for _ in range(n)]
visited[start[0]][start[1]] = 0
escape_possible = False

while q:
    x, y = q.popleft()
    
    # 출구에 도달한 경우
    if (x, y) == goal:
        # 유령이 없는 경우나, 유령이 있어도 남우가 더 빨리 도달한 경우
        if min_ghost_dist is None or visited[x][y] < min_ghost_dist:
            escape_possible = True
        break

    # 상하좌우 이동
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and visited[nx][ny] == float('inf'):
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

# 결과 출력
print("Yes" if escape_possible else "No")
