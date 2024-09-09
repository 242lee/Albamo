# 컴퓨터 수 N, 로그 수 M, 감염된 컴퓨터 수 K
N, M, K = map(int, input().split())
zombiePC = list(map(int, input().split()))

logs = []
for _ in range(M):
    logs.append(list(map(int, input().split())))

visited = [0] * (N + 1)
infected = [0] * (N + 1)

# 초기 감염된 컴퓨터 설정
for pc in zombiePC:
    infected[pc] = 1

# 로그를 시간 순서대로 정렬
logs.sort(key=lambda x: x[0])

# 모든 컴퓨터를 최초 감염원으로 가정하여 시뮬레이션
answer = 0
for i in range(1, N + 1):
    visited[i] = 1
    for t, a, b in logs:
        if visited[a]:
            visited[b] = 1
    
    # 전체 컴퓨터를 순회하면서 주어진 상태랑 같은지 확인
    flag = 1
    for j in range(1, N + 1):
        if visited[j] != infected[j]:
            flag = 0
            break
    
    # 순회를 다 하고 flag가 1이면 답이다.
    if flag:
        answer = i
        break
    # 아니면 다시 해
    else:
        visited = [0] * (N + 1)  # visited 배열을 리셋

print(answer)
