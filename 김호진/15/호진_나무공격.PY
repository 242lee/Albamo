import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
L1, R1 = map(int, input().split())
L2, R2 = map(int, input().split())

def attack(grid, L, R):
    # L~R에서 오른쪽으로 환경 파괴범(1)을 제거
    for row in range(L - 1, R):
        for col in range(m):
            if grid[row][col] == 1:
                grid[row][col] = 0  # 환경 파괴범 제거
                break  # 첫 번째 만난 환경 파괴범과 충돌했으므로 다음 행으로 넘어감

# 두 번의 공격
attack(grid, L1, R1)
attack(grid, L2, R2)

# 격자에 남아있는 환경 파괴범의 수
remaining_count = sum(row.count(1) for row in grid)
print(remaining_count)