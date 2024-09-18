from collections import deque

def solution(n, computers):
    ans = 0
    matrix = [0 for _ in range(n)]
    for cpu in range(n):
        if matrix[cpu] == 0:
            ans = ans + 1
            # matrix값 확인 결과 해당 컴퓨터를 확인한 적 없다면 bfs시작
            q = deque()
            q.append(cpu)
            matrix[cpu] = ans
            while len(q) > 0:
                current = q.popleft()
                for nxt in range(n):
                    if nxt != current:
                        if computers[current][nxt] == 1 and matrix[nxt] == 0:
                            matrix[nxt] = ans
                            q.append(nxt)
                if len(q) == 0:
                    break
    return ans
