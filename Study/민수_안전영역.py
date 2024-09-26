from collections import deque  # 큐를 사용하기 위해 deque 모듈을 불러옵니다

# BFS로 연결된 영역을 탐색하는 함수
def bfs(x, y, h, visited, graph):
    # 상하좌우 이동을 위한 좌표 변화량
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS 탐색을 위한 큐 초기화
    queue = deque()
    queue.append((x, y))  # 시작 좌표를 큐에 삽입
    visited[x][y] = True  # 현재 좌표 방문 처리
    
    while queue:
        x, y = queue.popleft()  # 큐에서 좌표를 꺼냅니다
        
        # 상하좌우로 이동하며 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 지도 내에 있고, 아직 방문하지 않았으며, 물에 잠기지 않은 경우에만 탐색
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny))  # 탐색할 좌표를 큐에 추가

# 입력 처리
n = int(input())  # 지도의 크기 입력
graph = [list(map(int, input().split())) for _ in range(n)]  # 지도 정보 입력

# 지도의 최소 높이와 최대 높이를 미리 계산 (이 높이 범위 내에서 물이 찰 수 있음)
min_height = min(map(min, graph))
max_height = max(map(max, graph))

result = 0  # 최대 안전 영역 개수를 저장할 변수

# 가능한 모든 비의 높이에 대해 안전 영역을 계산
for h in range(min_height - 1, max_height + 1):
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 기록하는 배열
    safe_areas = 0  # 현재 비의 높이에서의 안전 영역 개수
    
    # 지도의 모든 좌표를 탐색
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않았고, 물에 잠기지 않은 영역을 찾으면 BFS로 연결된 영역을 탐색
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited, graph)
                safe_areas += 1  # 탐색을 마친 하나의 안전 영역을 카운트
    
    # 현재 비의 높이에서 구한 안전 영역 개수와 최대값을 비교해 갱신
    result = max(result, safe_areas)

# 결과 출력
print(result)