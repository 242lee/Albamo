'''
예제 입력 1 
5 4 3
3 4 5
4 4 5
3 3 4
2 2 3
1 1 2

예제 출력 1 
3
'''
# 입력 받기
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))  # 감염된 컴퓨터 번호 리스트
logs = [list(map(int, input().split())) for _ in range(M)]  # 로그 리스트

# 감염 및 방문 리스트 초기화
infected = [False] * (N + 1)
visited = [False] * (N + 1)
result = 0

# 감염된 컴퓨터들 마킹
for pc in arr:
    infected[pc] = True

# 로그를 시간 순으로 정렬
logs.sort(key=lambda x: x[0])

# 1번부터 N번 컴퓨터 중 가장 먼저 감염된 컴퓨터를 찾는 과정
for i in range(1, N + 1):
    visited[i] = True  # i번 컴퓨터를 먼저 감염되었다고 가정
    
    # 로그의 시각 순서대로 파일 전송을 수행
    for t, a, b in logs:
        if visited[a]:  # a가 감염된 경우 b도 감염
            visited[b] = True
    
    # 감염 상태가 주어진 상태와 일치하는지 확인
    if visited == infected:
        answer = i
        break
    else:
        visited = [False] * (N + 1)  # visited 초기화

# 정답 출력
print(result)
