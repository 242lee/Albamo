class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 섬의 크기
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        
        # DFS 탐색 함수
        def dfs(ocean, x, y):
            # 현재 위치 방문 표시
            ocean.add((x, y))
            # 4방향 탐색 (상, 하, 좌, 우)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                # 유효한 위치인지 확인
                if 0 <= nx < m and 0 <= ny < n:
                    # 다음 칸이 더 높거나 같아야 물이 흐를 수 있음
                    if (nx, ny) not in ocean and heights[nx][ny] >= heights[x][y]:
                        dfs(ocean, nx, ny)

        # 태평양과 대서양으로 물이 흐를 수 있는 좌표 집합
        pacific = set()
        atlantic = set()

        # 태평양과 대서양 경계에서 DFS 시작
        for i in range(m):
            dfs(pacific, i, 0)  # 태평양 (왼쪽)
            dfs(atlantic, i, n - 1)  # 대서양 (오른쪽)
        for j in range(n):
            dfs(pacific, 0, j)  # 태평양 (위쪽)
            dfs(atlantic, m - 1, j)  # 대서양 (아래쪽)

        # 태평양과 대서양 모두에 도달 가능한 좌표의 교집합 반환
        return list(pacific & atlantic)
