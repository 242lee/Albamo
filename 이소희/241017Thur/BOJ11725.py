from collections import deque

N = int(input())
p = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    p[a].append(b)
    p[b].append(a)

# print(p)

parents = [0] * (N + 1)
visited = [0] * (N + 1)

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for next in p[now]:
            if not visited[next]:
                parents[next] = now
                visited[next] = 1
                q.append(next)

bfs(1)

for i in range(2, N + 1):
    print(parents[i])