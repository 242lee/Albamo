import sys

# 폭발 후 상태 계산 함수
def explode(grid):
    R, C = len(grid), len(grid[0])
    exploded = [['O'] * C for _ in range(R)]  # 기본적으로 모든 칸을 폭탄으로 초기화
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':  # 폭탄이 있는 칸
                exploded[r][c] = '.'
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        exploded[nr][nc] = '.'
    return exploded

# 입력 처리
input = sys.stdin.read
data = input().splitlines()
R, C, N = map(int, data[0].split())
initial_grid = [list(data[i + 1]) for i in range(R)]

if N == 1:  # 초기 상태 출력
    for row in initial_grid:
        print(''.join(row))
elif N % 2 == 0:  # 짝수 초 후에는 모든 칸에 폭탄
    for _ in range(R):
        print('O' * C)
else:
    # 3초 후 상태 계산
    second_grid = explode(initial_grid)
    third_grid = explode(second_grid)
    # 패턴에 따라 상태 선택
    if N % 4 == 3:
        for row in second_grid:
            print(''.join(row))
    elif N % 4 == 1:
        for row in third_grid:
            print(''.join(row))
