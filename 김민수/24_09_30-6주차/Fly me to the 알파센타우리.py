"""
리커젼 에러
"""
# def dfs(x, y, k, cnt):

#     # 도착지에 도착하면 탐색 종료
#     if x == y:
#         return cnt

#     # x가 y를 넘었으면 종료 (불필요한 경로 탐색 방지)
#     if x > y:
#         return float('inf')

#     # k는 현재 이동할 수 있는 거리
#     # 두 가지 경우로 재귀 호출 (한 칸 이동하고 k + 1, k - 1)
#     move1 = dfs(x + k, y, k + 1, cnt + 1)  # k+1
#     move2 = dfs(x + k, y, k, cnt + 1)      # k
#     move3 = dfs(x + k, y, k - 1, cnt + 1)  # k-1
    
#     # 최소 이동 횟수 반환
#     return min(move1, move2, move3)


# T = int(input())
# for _ in range(T):
#     x, y = map(int, input().split())
#     k = 0
#     cnt = 0
#     result = dfs(x, y, k, cnt)
#     print(result)

import math

def min_moves(x, y):
    distance = y - x
    # 이동할 수 있는 최대 거리를 구함. sqrt = 제곱근을 구하는 함수
    max_move = int(math.sqrt(distance))

    # max_move^2 == distance이면 이동 횟수는 2 * max_move - 1
    if max_move**2 == distance:
        return 2 * max_move - 1
    # max_move^2 < distance <= max_move^2 + max_move이면 이동 횟수는 2 * max_move
    elif max_move**2 < distance <= max_move**2 + max_move:
        return 2 * max_move
    # max_move^2 + max_move < distance이면 이동 횟수는 2 * max_move + 1
    else:
        return 2 * max_move + 1

T = int(input())  # 테스트 케이스 수 입력
for _ in range(T):
    x, y = map(int, input().split())
    print(min_moves(x, y))
