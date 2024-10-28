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
    if direction == 5 or direction == 6:
        treasure_x = max(treasure_x, compass_x + 1)
    if direction == 6 or direction == 8:
        treasure_y = min(treasure_y, compass_y + 1)
    if direction == 2 or direction == 4:
        treasure_y = max(treasure_y, compass_y + 1)

print(treasure_x, treasure_y)