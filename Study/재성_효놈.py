'''
gpt 풀이요
누가 먼저 움직이는지에 따라 최대 수확량이 바뀔 수 있으므로
순열을 사용해서 백트래킹 해야함
'''

import sys
input = sys.stdin.readline  # 입력 속도 향상을 위해 sys.stdin.readline 사용
from itertools import permutations  # 친구들의 순서를 바꾸기 위해 순열 사용

def dfs(grid, start, visited, time_visited):
    n = len(grid)  # 격자의 크기
    # 스택 초기화: (현재 위치, 경과 시간, 이동 경로, 현재까지의 수확량)
    stack = [(start, 0, [start], grid[start[0]][start[1]])]
    max_harvest = grid[start[0]][start[1]]  # 시작 위치의 수확량으로 초기화
    max_path = [start]  # 최대 수확량을 얻은 경로

    while stack:
        (x, y), time, path, harvest = stack.pop()  # 현재 상태 추출
        if time == 3:  # 3초가 지났다면
            if harvest > max_harvest:  # 현재까지의 수확량이 최대값보다 크면 갱신
                max_harvest = harvest
                max_path = path
            continue  # 다음 경로 탐색

        # 상, 하, 좌, 우, 현재 위치에 대해 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
            nx, ny = x + dx, y + dy  # 다음 위치 계산
            # 새 위치가 격자 내에 있고, 아직 방문하지 않은 위치인 경우
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                # 해당 시간에 다른 친구가 방문하지 않은 경우
                if (nx, ny, time+1) not in time_visited:
                    new_path = path + [(nx, ny)]  # 새 경로 생성
                    # 새 위치의 열매를 아직 수확하지 않았다면 수확량에 추가
                    new_harvest = harvest + (grid[nx][ny] if (nx, ny) not in path else 0)
                    stack.append(((nx, ny), time + 1, new_path, new_harvest))

    return max_harvest, max_path  # 최대 수확량과 그때의 경로 반환

def solve(n, m, grid, friends):
    max_total_harvest = 0  # 전체 최대 수확량

    # 친구들의 모든 가능한 순열에 대해 탐색
    for perm in permutations(range(m)):
        total_harvest = 0  # 현재 순열에서의 총 수확량
        visited = set()  # 전체 방문한 위치
        time_visited = set()  # 시간별 방문한 위치
        valid = True  # 현재 순열이 유효한지 확인하는 플래그

        for i in perm:  # 각 친구에 대해
            start = friends[i]  # 친구의 시작 위치
            if start in visited:  # 이미 방문한 시작점이면 무효
                valid = False
                break
            harvest, path = dfs(grid, start, visited, time_visited)  # DFS 수행
            total_harvest += harvest  # 수확량 누적
            visited.update(path)  # 전체 방문 위치 업데이트
            # 시간별 방문 위치 업데이트
            for t, (x, y) in enumerate(path):
                time_visited.add((x, y, t))

        if valid:  # 유효한 순열이면 최대 수확량 갱신
            max_total_harvest = max(max_total_harvest, total_harvest)

    return max_total_harvest  # 전체 최대 수확량 반환

# 입력 처리
n, m = map(int, input().split())  # 격자 크기와 친구 수 입력
# n x n 크기의 격자 정보 입력
grid = [list(map(int, input().split())) for _ in range(n)]
# 친구들의 시작 위치 입력 (0-based 인덱스로 변환)
friends = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# 결과 출력
print(solve(n, m, grid, friends))  # 최대 수확량 계산 및 출력
