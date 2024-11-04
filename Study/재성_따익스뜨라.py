from heapq import heappush, heappop

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    q = []
    distance = [int(1e9)]*(n+1)
    distance[1] = 0
    heappush(q, (0, 1))
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for g in graph[now]:
            cost = dist + 1
            if cost < distance[g]:
                distance[g] = cost
                heappush(q, (cost, g))     
    
    distance[0] = 0
    m = max(distance)
    answer = distance.count(m)

    return answer
