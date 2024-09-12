'''
같은 색의 보도블록만 밟아서
N행 M열에 도착해야해
빨간색 또는 회색으로 이루어져있어
현재 밟고 있는 색의 보도블록만 밟아
점프력은 x
사망하지 않고 도착할 수 있는가
BFS로구나..
BFS 강의 다시 들으면서 풀었음
'''

from collections import deque

n = int(input())
m = int(input())

# 등교길 생성
road = [list(map(int, input().split())) for _ in range(n)] 
color = road[0][0] # 출발지의 색깔
visited = [[-1 for _ in range(m)] for _ in range(n)] # 방문처리할 배열 생성
jump = int(input()) # 점프할 수 있는 거리

# 만약 출발지의 색깔과 도착지의 색깔이 다르면 사망
if road[0][0] != road[n-1][m-1]:
    print("DEAD")
    exit()

# 큐 생성 후 큐에 출발지점을 삽입하고 출발지점 방문처리
q = deque()
q.append((0,0))
visited[0][0] = 1

# 이제 큐를 하나씩 빼가며 그 주변 탐색
while q:
    a, b = q.popleft()
    # 점프할 수 있는 범위
    for dy in range(-jump, jump+1):
        for dx in range(-jump, jump+1):
            # 대각선 조건 추가
            if abs(dy) + abs(dx) <= jump:
                cy = dy + a
                cx = dx + b
                # 범위 내에 있고 색깔이 사망하는 색이 아니고 방문을 하지 않았으면
                if ( 0 <= cy < n ) and ( 0 <= cx < m ):
                    if ( road[cy][cx] == color ) and ( visited[cy][cx] == -1 ):
                        # 도착지점까지 왔으면
                        if ( cy == n-1 ) and ( cx == m-1 ):
                            print("ALIVE") # 살았다
                            exit()
                    # 도착지점이 아니면 방문처리 후 큐에 삽입
                        visited[cy][cx] = 1
                        q.append(( cy, cx )) 

print("DEAD")