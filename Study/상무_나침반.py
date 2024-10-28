# 1, 3, 5, 7은 영역이 아니고 선을 제어한다.
# 2, 4, 6, 8은 각각 오른쪽위 오른쪽아래 왼쪽아래 왼쪽위를 제어한다.
# 그러므로 1, 3, 5, 7은 x혹은 y의 좌표를 확정지어준다.
# 2, 4, 6, 8은 영역을 알려주므로 2는 나침반보다 위쪽에 있다는 뜻이므로 보물 위치랑 나침반의 위쪽을 비교해서 작은 값으로 보물 위치를 옮긴다.
# 2와 8은 같은 개념(나침반보다 위쪽), 4와 6은 같은 개념(나침반보다 아래쪽)
# 2와 4는 같은 개념(나침반보다 오른쪽), 6와 8은 같은 개념(나침반보다 왼쪽)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
treasure_x, treasure_y = 1, 1

for _ in range(M):
    compass_x, compass_y, direction = map(int, input().split())
    
    if direction == 1 or direction == 5:
        treasure_y = compass_y
    if direction == 3 or direction == 7:
        treasure_x = compass_x
    if direction == 2 or direction == 8:
        treasure_x = min(treasure_x, compass_x + 1)
    if direction == 4 or direction == 6:
        treasure_x = max(treasure_x, compass_x + 1)
    if direction == 6 or direction == 8:
        treasure_y = min(treasure_y, compass_y + 1)
    if direction == 2 or direction == 4:
        treasure_y = max(treasure_y, compass_y + 1)

print(treasure_x, treasure_y)