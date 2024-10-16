# H를 기준으로 좌우로 K칸 만큼을 순회하고집을 수 있는 로봇의 index값을 저장할 수 있으면 어떨까?
# 1, 3  1, 3, 4    3, 4, 5, 6
# 겹치는 것에대한 비교를 해주는 과정이 까다로워질듯.

# 기계와 로봇의 index를 각각 뽑아서 거리값 k와 비교한다면 어떨까 ?

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
line = input().strip()

# 로봇과 부품 위치저장
robots = []
parts = []

for i in range(n):
    if line[i] == 'P':
        robots.append(i)
    elif line[i] == 'H':
        parts.append(i)

part_idx = 0
robot_idx = 0
matched_count = 0

while robot_idx < len(robots) and part_idx < len(parts):
    robot_pos = robots[robot_idx]
    part_pos = parts[part_idx]

    # 로봇이 부품을 집을 수 있는 경우
    if abs(robot_pos - part_pos) <= k:
        matched_count += 1
        robot_idx += 1
        part_idx += 1
    # 로봇 위치가 더 뒤에 있다면 부품 인덱스 증가
    elif robot_pos > part_pos:
        part_idx += 1
    # 부품 위치가 더 뒤에 있다면 로봇 인덱스 증가
    else:
        robot_idx += 1

print(matched_count)
