import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

ing = deque([-1] * W)
visited = [0] * N # 종료조건
muge = 0  # 다리 위 트럭들의 하중
time = 0   # 시간초
idx = 0   # 다음으로 다리에 넣어야 할 트럭 인덱스

# 모두 다리 통과하면 종료
while sum(visited) < N:
    time += 1
    # 다리 맨 앞에 있는 인덱스
    first = ing[0]

    # 다리 끝에 도달한 트럭이 있다면 빼기
    if first > -1:
        ing[0] = -1  # 인덱스 초기화
        muge -= trucks[first]  # 다리 위에 있는 트럭 무게도 빼기
        visited[first] = 1   # 다리 통과

    # 나머지 트럭들도 이동시킴
    ing.rotate(-1)

    # 남은 트럭이 있고, 하중 견딜 수 있으면 다리에 넣기
    if idx < N and muge + trucks[idx] <= L:
        ing[W-1] = idx   # 다리에 넣고
        muge += trucks[idx]   # 무게 증가
        idx += 1   # 다음 트럭 인덱스도 증가

print(time)
