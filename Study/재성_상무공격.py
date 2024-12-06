import sys

def attack(grid, L, R, m):
    """
    특정 행 범위(L~R)에서 투사체를 오른쪽으로 진행하며
    첫 번째로 만난 환경 파괴범을 제거한다.
    """
    for row in range(L - 1, R):  # 행 범위는 1-indexed이므로 0-index로 맞춤
        for col in range(m):
            if grid[row][col] == 1:
                grid[row][col] = 0  # 환경 파괴범 제거
                break  # 한 번 만난 후 멈춤

def count_remaining(grid):
    """
    격자 내 남아있는 환경 파괴범의 수를 세는 함수.
    """
    return sum(row.count(1) for row in grid)

def main():
    input = sys.stdin.readline  # 표준 입력
    # 격자의 크기 n, m 읽기
    n, m = map(int, input().strip().split())
    # 격자 정보 읽기
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    
    # 첫 번째 공격 정보 읽기
    L1, R1 = map(int, input().strip().split())
    # 두 번째 공격 정보 읽기
    L2, R2 = map(int, input().strip().split())
    
    # 첫 번째 공격 수행
    attack(grid, L1, R1, m)
    # 두 번째 공격 수행
    attack(grid, L2, R2, m)
    
    # 남아있는 환경 파괴범의 수 출력
    print(count_remaining(grid))

if __name__ == "__main__":
    main()
