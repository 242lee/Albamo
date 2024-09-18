from collections import deque

def solution(n, computers):            
    
    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                     q.append(a)
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer

'''
def solution(n, computers):            
    
    def dfs(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                dfs(a)      
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer
'''