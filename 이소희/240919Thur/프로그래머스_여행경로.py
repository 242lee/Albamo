from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    
    for start in routes:
        routes[start].sort(reverse=True)
        # {'ATL': ['ICN', 'SFO']} -> {'ATL': ['SFO', 'ICN']}
        
    route = []
    
    def dfs(now):
        # 현재 공항에서 갈 수 있는 곳
        while routes[now]:
            next = routes[now].pop()
            dfs(next)
            route.append(next)
        
    dfs("ICN")
    
    route = route + ["ICN"]
    return route[::-1]