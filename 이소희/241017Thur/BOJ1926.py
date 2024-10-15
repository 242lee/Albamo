directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def dfs(p, q):
    cnt = 0
    stack = [(p, q)]
    visited[p][q] = 1
    cnt += 1
    while stack:
        ci, cj = stack.pop()    
        for dir in directions:
            ni, nj = ci + dir[0] , cj + dir[1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == '1':
                visited[ni][nj] = 1
                stack.append((ni, nj))
                cnt += 1
    return cnt

sizes = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '1' and not visited[i][j]:
            size = dfs(i, j)
            sizes.append(size)

print(len(sizes))
print(max(sizes) if sizes else 0)