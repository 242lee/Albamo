# BJ 로그프레소 마에스트로

## 문제
백준 31937번 문제, **"로그프레소 마에스트로"**는 여러 컴퓨터 간의 파일 전송 기록이 주어지고, 일부 컴퓨터가 감염된 상태에서, **최초로 감염된 컴퓨터를 찾는 문제**입니다. 각 로그는 특정 시간에 두 컴퓨터 간 파일 전송을 나타내며, 감염된 컴퓨터가 다른 컴퓨터로 감염을 전파할 수 있습니다. 문제는 감염 경로를 추적하여, 처음으로 감염된 컴퓨터를 식별하는 것이 목표입니다. **그래프 탐색과 로그 분석**이 필요한 문제입니다.

## 풀이 코드 - DFS

```python
import sys
input = sys.stdin.readline

def find_infected_computer_dfs(N, M, K, infected_list, logs):
    # 감염된 컴퓨터 배열 초기화
    infected = [False] * (N + 1)
    for computer in infected_list:
        infected[computer] = True  # 감염된 컴퓨터 표시
    
    # 로그를 시간 순서대로 정렬
    logs.sort(key=lambda x: x[0])

    # DFS 탐색 함수 정의
    def dfs(visited, i):
        visited[i] = True  # 현재 컴퓨터를 방문 처리
        for time, a, b in logs:  # 각 로그에 대해 처리
            if visited[a] and infected[a]:  # a 컴퓨터가 감염되어 있고 방문했다면
                visited[b] = True  # b 컴퓨터도 감염되므로 방문 처리

    # 모든 컴퓨터를 최초 감염원으로 가정하고 탐색
    for i in range(1, N + 1):
        if not infected[i]:
            continue  # 감염되지 않은 컴퓨터는 스킵
        
        visited = [False] * (N + 1)  # 방문 배열 초기화
        dfs(visited, i)  # DFS로 감염 경로 추적
        
        # 모든 컴퓨터의 감염 상태가 예상한 것과 일치하는지 확인
        if all(infected[j] == visited[j] for j in range(1, N + 1)):
            print(i)  # 최초 감염원 출력
            return

# 입력 처리
N, M, K = map(int, input().split())  # N: 컴퓨터 수, M: 로그 수, K: 감염된 컴퓨터 수
infected_list = list(map(int, input().split()))  # 감염된 컴퓨터 목록
logs = [tuple(map(int, input().split())) for _ in range(M)]  # 로그 목록

find_infected_computer_dfs(N, M, K, infected_list, logs)

```