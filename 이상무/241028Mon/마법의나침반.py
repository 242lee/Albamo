import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 보물의 최종 위치를 결정할 후보 좌표
treasure_x, treasure_y = 1, 1

# 나침반 기록을 이용하여 보물 위치 범위 좁히기
for _ in range(M):
    compass_x, compass_y, direction = map(int, input().split())
    
    # 각 방향에 따라 보물 위치를 제한
    if direction == 1 or direction == 5:  # 위 또는 아래 방향
        treasure_y = compass_y
    if direction == 3 or direction == 7:  # 오른쪽 또는 왼쪽 방향
        treasure_x = compass_x
    if direction == 2 or direction == 8:  # 오른쪽 위 또는 왼쪽 위 대각선 방향
        treasure_x = min(treasure_x, compass_x + 1)
    if direction == 5 or direction == 6:  # 아래 또는 왼쪽 아래 대각선 방향
        treasure_x = max(treasure_x, compass_x + 1)
    if direction == 6 or direction == 8:  # 왼쪽 아래 또는 왼쪽 위 대각선 방향
        treasure_y = min(treasure_y, compass_y + 1)
    if direction == 2 or direction == 4:  # 오른쪽 위 또는 오른쪽 아래 대각선 방향
        treasure_y = max(treasure_y, compass_y + 1)

# 최종 보물 위치 출력
print(treasure_x, treasure_y)
