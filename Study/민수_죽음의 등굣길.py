"""
같은 색의 보도블록만 밟으면서 이동. 다른 색의 보도블럭을 밟으면 사망
1행 1열에서 출발해 N행 M열에 도착해야 한다.

빨간색 또는 회색으로 이루어진 등굣길을 이동하면서 현재 밟고 있는 보도블럭과
같은 색의 보도블록만 밟고 이동해야 한다.

점프력은 X이기 때문에 X 이하인 보도블록으로만 이동할 수 있음
"""
# 입력
"""
첫째 줄에 등굣길의 행의 개수 
N이 주어진다. 

둘째 줄에 등굣길의 열의 개수 
M이 주어진다. 

셋째 줄부터 
N개의 줄에 걸쳐 
i + 2번째 줄에 i번째 행의 보도블록의 색깔을 나타내는 
M개의 정수가 열 순서대로 공백으로 구분되어 주어진다. 
0인 경우 빨간색 보도블록, 
1인 경우 회색 보도블록이라는 것을 의미한다.

마지막 줄에 지훈이의 점프력을 나타내는 정수 X가 주어진다.
"""
from collections import deque

# 입력 받기
n = int(input())  # 행의 개수
m = int(input())  # 열의 개수

# 등교길 생성
road = [list(map(int, input().split())) for _ in range(n)]
color = road[0][0]  # 출발지의 색깔
visited = [[-1 for _ in range(m)] for _ in range(n)]  # 방문 처리 배열 생성
jump = int(input())  # 점프할 수 있는 거리

# 출발지와 도착지의 색깔이 다르면 즉시 사망
if road[0][0] != road[n - 1][m - 1]:
    print("DEAD")
    exit()

# 큐 생성 및 출발 지점을 삽입하고 방문 처리
q = deque()
q.append((0, 0))
visited[0][0] = 1  # 시작점 방문 처리

# BFS 탐색 시작
while q:
    a, b = q.popleft()

    # 점프할 수 있는 범위 내에서 상하좌우 및 대각선 탐색
    for dy in range(-jump, jump + 1):
        for dx in range(-jump, jump + 1):
            # 대각선 및 상하좌우 조건 처리
            if abs(dy) + abs(dx) <= jump:
                cy = a + dy
                cx = b + dx

                # 경계 내에 있고, 색이 같으며 아직 방문하지 않은 경우
                if 0 <= cy < n and 0 <= cx < m and road[cy][cx] == color and visited[cy][cx] == -1:
                    # 도착지에 도달하면 ALIVE 출력 후 종료
                    if cy == n - 1 and cx == m - 1:
                        print("ALIVE")
                        exit()

                    # 방문 처리 후 큐에 추가
                    visited[cy][cx] = 1
                    q.append((cy, cx))

# 도착하지 못했으면 DEAD 출력
print("DEAD")

