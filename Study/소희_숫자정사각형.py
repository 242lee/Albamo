'''
메모리 31120KB 속도 56ms
'''
N, M = map(int, input().split())
bd = list(input() for _ in range(N))

area = 1

for i in range(N):
    for j in range(M):
        for k in range(1, min(N, M)):   # k 이내에서 증가시켜보면서 
            if i + k < N and j + k < M: # 범위 이내에 있으면
                if bd[i][j] == bd[i][j+k] == bd[i+k][j] == bd[i+k][j+k]:
                    area = max(area, (k + 1) ** 2)

print(area)
