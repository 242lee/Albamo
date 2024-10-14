# 유령과 남우 bfs 돌려서 경로가 겹치면 NO 안겹치면 YES
# 아예 출구를 못찾는 경우도 NO
# 유령은 벽뚫 가능
# 그러면 유령의 최단 거리 보다 남우의 최단 거리가 더 길면 무조건 NO

# 그렇다면 생각해야 할 것은 
# 1. bfs를 사용해서 남우의 최단 시간을 구한다. 출구에 도착할 수 있는지 없는지 여부 파악.
# 2. 1.번이 만족했다면 유령의 최단 시간보다 남우의 최단 시간이 더 짧은지 여부 파악.

from collections import deque

# BFS 탐색 함수
def bfs(start_position, maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = [[float('inf')] * m for _ in range(n)]
    queue = deque([start_position])
    distances[start_position[0]][start_position[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#':
                if distances[nx][ny] == float('inf'):
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))
    
    return distances

# 유령 최소거리 찾는 함수
def ghost_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def can_escape(maze, n, m):
    # 남우 위치, 출구 위치, 유령 위치 찾기
    namu_pos = None
    exit_pos = None
    ghost_positions = []
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'N':
                namu_pos = (i, j)
            elif maze[i][j] == 'D':
                exit_pos = (i, j)
            elif maze[i][j] == 'G':
                ghost_positions.append((i, j))
    
    # 남우의 최단 거리 구하기
    namu_distances = bfs(namu_pos, maze, n, m)
    exit_namu_dist = namu_distances[exit_pos[0]][exit_pos[1]]
    
    # 남우가 출구에 도달할 수 없는 경우
    if exit_namu_dist == float('inf'):
        return "No"
    
    # 각 유령에 대해 출구와의 거리 계산
    for ghost_x, ghost_y in ghost_positions:
        ghost_dist_to_exit = ghost_distance(ghost_x, ghost_y, exit_pos[0], exit_pos[1])
        if ghost_dist_to_exit <= exit_namu_dist:
            return "No"
    
    return "Yes"

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

# 탈출 가능 여부 확인
print(can_escape(maze, n, m))
