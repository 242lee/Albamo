# 프로그래머스 가장 먼 노드
from collections import deque

'''
1. 간선 간의 길을 탐색해야 하므로 간선 정보를 node에 넣어야함
2. 최대 거리를 구해야 하는데, 탐색 과정에서 루프가 생기지 않아야하므로 
   거리 탐색 + 중복 제외가 되는 bfs를 선택함
'''

# 2 <= n <= 20,000 / 1 <= edge <= 5,000
def solution(n, edge):
    node = [[] for _ in range(n+1)]
    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])

    v = [-1] * (n+1)
    v[1] = 0
    max_dist = 0
    answer = -1
    dq = deque([1])
    while dq:
        t = dq.popleft()
        if max_dist == v[t]:
            answer += 1
        elif max_dist < v[t]:
            max_dist = v[t]
            answer = 1
        for nt in node[t]:
            if v[nt] == -1:
                v[nt] = v[t] + 1
                dq.append(nt)
    
    return answer

# return 3
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))