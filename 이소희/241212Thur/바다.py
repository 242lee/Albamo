'''
heights: m x n 크기의 2D 리스트로, 각 좌표에서의 고도를 나타냅니다.
예: heights = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
목표

Pacific(태평양)과 Atlantic(대서양) 두 바다로 물이 흐를 수 있는 모든 좌표를 찾습니다.
물은 상하좌우로 이동할 수 있으며, 낮은 지점에서 높은 지점으로는 이동할 수 없습니다.
출력: 물이 두 바다로 모두 흐를 수 있는 좌표의 리스트.
바다와 접하는 좌표

태평양(Pacific):
왼쪽 열(0열)과 윗 행(0행).
대서양(Atlantic):
오른쪽 열(n-1열)과 아랫 행(m-1행).
예제 이해

heights = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
result = [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]는 아래 조건을 만족:
물이 태평양과 대서양으로 모두 흐를 수 있음.
'''

def pacificAtlantic(heights):
    if not heights:
        return []
    
    m, n = len(heights), len(heights[0])
    
    pacific_reachable = set()
    atlantic_reachable = set()
    
    def dfs(x, y, reachable, prev_height):
        if (x, y) in reachable or x < 0 or y < 0 or x >= m or y >= n or heights[x][y] < prev_height:
            return
        reachable.add((x, y))
        dfs(x + 1, y, reachable, heights[x][y])
        dfs(x - 1, y, reachable, heights[x][y])
        dfs(x, y + 1, reachable, heights[x][y])
        dfs(x, y - 1, reachable, heights[x][y])

    # 태평양 탐색: 위쪽 행과 왼쪽 열에서 시작
    for i in range(m):
        dfs(i, 0, pacific_reachable, heights[i][0])  # 왼쪽 열
        dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])  # 오른쪽 열
    for j in range(n):
        dfs(0, j, pacific_reachable, heights[0][j])  # 윗 행
        dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])  # 아랫 행

    # 교집합 계산 및 리스트로 변환
    result = list(pacific_reachable & atlantic_reachable)
    result.sort()  # 정렬
    result = [list(coord) for coord in result]  # 튜플을 리스트로 변환
    
    return result

# 테스트
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))  # 출력: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
