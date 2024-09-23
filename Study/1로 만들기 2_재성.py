from collections import deque
import sys
input = sys.stdin.readline

def bfs_min_operations(N):
    # 각 숫자까지 가는 최소 연산 횟수를 기록하는 리스트
    dp = [-1] * (N + 1)
    dp[1] = 0  # 1에서 1까지는 연산이 0번 필요함

    # BFS를 위한 큐
    queue = deque([1])

    # 경로를 추적하기 위한 리스트
    path = [-1] * (N + 1)

    while queue:
        current = queue.popleft()

        # 현재 숫자에서 다음 가능한 세 가지 연산을 적용
        for next_num in [current * 3 if current * 3 <= N else None,
                         current * 2 if current * 2 <= N else None,
                         current + 1 if current + 1 <= N else None]:
            if next_num is not None and dp[next_num] == -1:  # 아직 방문하지 않은 숫자인 경우
                dp[next_num] = dp[current] + 1  # 연산 횟수 증가
                path[next_num] = current  # 어디서 왔는지 기록
                queue.append(next_num)

        # N에 도달한 경우 BFS 종료
        if dp[N] != -1:
            break

    # 연산 횟수 출력
    print(dp[N])

    # 경로 출력 (N으로 만드는 과정 추적)
    result_path = []
    current = N
    while current != -1:
        result_path.append(current)
        current = path[current]

    # 경로를 순서대로 출력
    print(' '.join(map(str, result_path)))

# 입력 받기
N = int(input())

# 결과 출력
bfs_min_operations(N)
