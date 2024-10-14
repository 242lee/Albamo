# 입력을 받기 위한 부분
n, m = map(int, input().split())
fruits_map = [list(map(int, input().split())) for _ in range(n)]
friends = [tuple(map(int, input().split())) for _ in range(m)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 열매 수확량을 저장할 변수
max_fruit_sum = 0

# DFS 함수 정의
def dfs(f_idx, positions, fruit_sum, visited):
    global max_fruit_sum
    
    # 모든 친구들에 대해 이동이 끝났을 때, 최대 열매 수확량 갱신
    if f_idx == m:
        max_fruit_sum = max(max_fruit_sum, fruit_sum)
        return

    # 현재 친구의 위치
    x, y = positions[f_idx]
    
    # 시작 위치에서 바로 열매를 수확
    initial_fruit = fruits_map[x][y]
    
    # 현재 위치 방문 체크
    visited[x][y] = True
    # 다음 친구를 위한 DFS 호출
    dfs(f_idx + 1, positions, fruit_sum + initial_fruit, visited)
    
    # 현재 위치 방문 해제
    visited[x][y] = False
    
    # 4방향 이동하면서 DFS 호출
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 방문 체크
            visited[nx][ny] = True
            # 다음 위치로 이동 후, 다음 친구에 대해 DFS 호출
            new_positions = positions[:f_idx] + [(nx, ny)] + positions[f_idx+1:]
            dfs(f_idx + 1, new_positions, fruit_sum + initial_fruit + fruits_map[nx][ny], visited)
            # 방문 해제 (백트래킹)
            visited[nx][ny] = False

# 방문 배열 초기화
visited = [[False] * n for _ in range(n)]

# 친구들의 초기 위치로부터 DFS 시작
initial_positions = [(x - 1, y - 1) for x, y in friends]
dfs(0, initial_positions, 0, visited)

print(max_fruit_sum)
