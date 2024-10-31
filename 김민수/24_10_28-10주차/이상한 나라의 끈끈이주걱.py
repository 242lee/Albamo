"""
x좌표의 차이보다 y좌표에 아래에서 솟은 끈끈이는 +1
위에서 솟은 끈끈이는 -1 하여 차이가 같거나 작다면
stay. 크면 adios

하나의 끈끈이만 있을 경우 0,0을 기준으로 똑같이 계산

출구의 위치 N, 끈끈이주걱의 개수 M

7 2
0 2 2
1 5 1
"""

import sys
input = sys.stdin.readline

# 출구 위치 N과 끈끈이 주걱의 개수 M을 입력받음
N, M = map(int, input().split())

# 각 끈끈이 주걱의 정보를 저장할 리스트
sticky_traps = []
for _ in range(M):
    c, x, h = map(int, input().split())
    sticky_traps.append((c, x, h))  # (c: 방향, x: 위치, h: 높이)

# 끈끈이들을 x 좌표 기준으로 정렬하고 도착점 추가
sticky_traps.sort(key=lambda trap: trap[1])
sticky_traps.append((-1, N, 0))  # 도착점 추가

# 초기 위치와 y 좌표 설정
current_x, current_y = 0, 0  # 시작 위치는 (0, 0)
result = "stay"

# 각 끈끈이 구간에 대해 이동 가능 여부 확인
for c, x, h in sticky_traps:
    distance_x = x - current_x  # x 좌표 이동 거리

    # 아래에서 솟은 끈끈이 주걱 처리 (c = 0)
    if c == 0:
        # 파리가 끈끈이 높이보다 정확히 1 큰 위치로 이동 가능해야 함
        if current_y < h + 1:
            current_y = h + 1  # y 좌표 갱신

    # 위에서 내려온 끈끈이 주걱 처리 (c = 1)
    elif c == 1:
        # 현재 위치에서 내려가는 범위가 -1씩만 가능하므로 이동 가능한지 확인
        if current_y - distance_x > h - 1:
            result = "adios"
            break
        current_y = h - 1  # y 좌표 갱신하여 끈끈이를 피함

    # 도착점에 도달하는 경우 처리
    elif c == -1:
        # 출구까지 정확히 y=0에 도달 가능한지 확인
        if current_y > distance_x or (current_y - distance_x) % 2 != 0:
            result = "adios"
            break

    # x 좌표 갱신
    current_x = x

# 최종 결과 출력
print(result)

