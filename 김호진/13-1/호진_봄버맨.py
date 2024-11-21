# 백준 16918 봄버맨 실버1
import sys
input = sys.stdin.readline

# 1 ~ 200
R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]


def solution():
    # 1. N == 1일 때: 초기 상태 그대로 출력
    if N == 1:
        return arr

    # 2. N % 2 == 0일 때: 모든 칸에 폭탄이 있는 상태
    if N % 2 == 0:
        return [['O'] * C for _ in range(R)]

    # 초기 폭탄 위치 탐색
    first_bombs = find_bombs(arr)

    # 3. N % 4 == 3일 때: 초기 폭탄 터진 상태
    if N % 4 == 3:
        return explosion(first_bombs)

    # 4. N > 1이고 N % 4 == 1일 때: 두 번째 폭발 후 상태
    if N % 4 == 1:
        # 첫 폭발 이후 남은 폭탄들이 두 번째 터질 폭탄들임
        after_first_explosion_arr = explosion(first_bombs)
        second_bombs = find_bombs(after_first_explosion_arr)
        return explosion(second_bombs)

def find_bombs(arr):
    bombs = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bombs.append((i, j))
    return bombs

def explosion(bombs):
    ans = [['O'] * C for _ in range(R)]
    for x, y in bombs:
        ans[x][y] = '.'
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                ans[nx][ny] = '.'
    return ans

# 출력
ans = solution()
for row in ans:
    print(*row, sep='')
