# K 부품을 잡을 수 있는 거리
N, K =  map(int, input().split())
line = list(input())
# H 부품 P 로봇

visited = [0] * N
for i in range(N):
    if line[i] == 'P' and not visited[i]:  # 로봇이 나오면
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if line[j] == 'H' and not visited[j]:
                visited[i] = 1
                visited[j] = 1
                break

cnt = 0
for k in range(N):
    if line[k] == 'P' and visited[k]:
        cnt += 1

print(cnt)