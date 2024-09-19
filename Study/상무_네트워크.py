# dfs 풀이 어떻게 했더라.
# visited를 False로 초기화
# visited를 순회하면서 False이면 dfs 실행
# 재귀로 풀었음.

def dfs(com, computers, visited):
    visited[com] = True

    for idx, value in enumerate(computers[com]):
        if value and not visited[idx]:
            dfs(idx, computers, visited)


def solution(n, computers):
    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            cnt += 1

    return cnt