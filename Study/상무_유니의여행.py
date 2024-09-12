# 초기 기력이 5 이하이기 때문에 아이템은 최대 2번밖에 쓰지 못한다 어떠한 경우에도.
# 접근 1.
# 1. 0, 0 을 초기 위치 x, y로 잡고 goal_x, goal_y가 도착 위치로 잡는다.
# 2. 초기 위치에서 (1, 0), (-1, 0), (0, 1), (0, -1)을 더해보고, 초기 위치에서 items의 값들을 일일이 더해본다.
# 3. 만약 items값을 더했을 때 goal_x, goal_y에 도착했으면, k 값에 2를 더해주고,
# 4. (1, 0), (-1, 0), (0, 1), (0, -1)을 더했을 때, goal_x, goal_y에 도착했으면, k 값에 1을 더해준다.
# 5. 여기서 items랑 (1, 0), (-1, 0), (0, 1), (0, -1)을 더했을 경우 두가지 다 goal_x, goal_y에 도착하면 k 값에 1을 더해준다.
# 6. 만약 3,4 번에서 goal_x, goal_y값에 도착하지 않았으면 초기 위치에서 더한 값들을 nx, ny로 이동 시켜보고, goal_x, goal_y값과 비교해서 가장 가까운 값으로 x, y를 이동시킨다.
# 7. 6에서 판단한 가장 거리가 짧은 값을 초기 위치 x, y로 잡고 반복한다.
# 위와 같이 생각해보면, 반례가 엄청 많다.
# 예를 들면 0, 0 초기위치  10, 10 goal_x, goal_y 고 아이템이 0, 10000  10, -9990 이면 한 칸씩 이동할 것이다.
# 
# 접근 2.
# 기력 = 1, 2, 3, 4, 5
# 기력 = 1 : 최대 아이템 0
# 기력 = 2, 3 : 최대 아이템 1
# 기력 = 4, 5 : 최대 아이템 2

import sys
input = sys.stdin.readline

# 아이템의 개수와 초기 기력 입력
num_items, initial_energy = map(int, input().split())

# 아이템 좌표 입력
item_coordinates = [tuple(map(int, input().split())) for _ in range(num_items)]

# 목적지 좌표 입력
destination_x, destination_y = map(int, input().split())

# 초기값 설정: 목적지까지 직접 이동하는 경우의 기력 소모
min_energy_required = abs(destination_x) + abs(destination_y)

# 목적지와 각 아이템 좌표의 상대 좌표를 저장할 집합
relative_positions = set()

# 아이템 좌표로부터 목적지의 상대 좌표 계산
for item_x, item_y in item_coordinates:
    relative_positions.add((destination_x - item_x, destination_y - item_y))

# 아이템 사용과 이동을 고려한 최소 기력 소모 계산
for item_x, item_y in item_coordinates:
    # 아이템을 사용하고 목적지까지 이동하는 경우의 기력 소모
    energy_with_item = abs(destination_x - item_x) + abs(destination_y - item_y) + 2
    min_energy_required = min(min_energy_required, energy_with_item)
    
    # 아이템 위치와 목적지의 상대 좌표가 일치하는 경우
    if (item_x, item_y) in relative_positions:
        min_energy_required = min(min_energy_required, 4)
    
    # 아이템의 인접한 칸으로 이동하는 경우를 고려
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (item_x + dx, item_y + dy) in relative_positions:
            min_energy_required = min(min_energy_required, 5)

# 최종 기력 소모가 초기 기력 이내인 경우 출력, 그렇지 않으면 -1 출력
if min_energy_required <= initial_energy:
    print(min_energy_required)
else:
    print(-1)

# from collections import deque

# def bfs_min_energy(N, K, items, destination):
#     # 출발지와 목적지
#     start = (0, 0)
#     Ex, Ey = destination
    
#     # BFS를 위한 큐와 방문 체크
#     queue = deque([(0, 0, K)])  # (x좌표, y좌표, 남은 기력)
#     visited = set([(0, 0, K)])
    
#     # BFS 실행
#     while queue:
#         x, y, energy = queue.popleft()
        
#         # 목적지에 도착했으면 현재까지 소비한 기력을 반환
#         if (x, y) == (Ex, Ey):
#             return K - energy
        
#         # 남은 기력이 없으면 탐색 중단
#         if energy <= 0:
#             continue
        
#         # 1칸 이동 (x방향 또는 y방향으로)
#         for dx, dy in [(1, 0), (0, 1)]:
#             nx, ny = x + dx, y + dy
#             if (nx, ny, energy - 1) not in visited and energy - 1 >= 0:
#                 visited.add((nx, ny, energy - 1))
#                 queue.append((nx, ny, energy - 1))
        
#         # 아이템 사용
#         for ax, by in items:
#             nx, ny = x + ax, y + by
#             if (nx, ny, energy - 2) not in visited and energy - 2 >= 0:
#                 visited.add((nx, ny, energy - 2))
#                 queue.append((nx, ny, energy - 2))
    
#     # 목적지에 도달할 수 없는 경우
#     return -1

# # 최소 기력 소모 결과 출력
# print(bfs_min_energy(N, K, items, destination))
