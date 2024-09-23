# 백준 31885 Yunny's Trip 골3
import sys
input = sys.stdin.readline

# N(1~2*10^5), K(1~5)
N, K = map(int, input().split())
# -10^12~10^12
items = [list(map(int, input().split())) for _ in range(N)]
# -10^12~10^12
end_x, end_y = map(int, input().split())

# 목적지까지 기본이동 시 기력량
ans = abs(end_x) + abs(end_y)

# 두번째 아이템을 썼을 때 목적지에 도착할 수 있는 좌표들
second_item = set()
for x, y in items:
    second_item.add((end_x - x, end_y - y))

for x, y in items:
    # 목적지까지 기본이동 시 기력량 vs
    # 첫 아이템 사용해서 (x, y)로 이동 + 남은 거리 기본이동 시 기력량
    ans = min(ans, 2 + abs(end_x - x) + abs(end_y - y))
    # 두번째 아이템 사용해서 목적지 도착 가능하면
    if (x, y) in second_item:
        # 남은 거리 기본이동 시 기력량 vs 두번째 아이템 쓴 기력량
        ans = min(ans, 4)
    
    # 첫 아이템을 쓰고(x, y)
    # 상하좌우 한 칸 이동 후의 좌표(x + dx, y + dy)가
    # 두번째 아이템을 썼을 때 목적지에 도착 가능하면
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        if (x + dx, y + dy) in second_item:
            ans = min(ans, 5)

print(ans if ans <= K else -1)