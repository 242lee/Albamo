# 1. input값을 받고, 사용하기 편하게 데이터 수정
N, M = map(int,input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

# 2. dfs를 정의한다. prev값을 활용하여 이전과 동일한 move가 불가능 하도록 한다.
def dfs(ci, cj, used, prev):
    global gas
    if ci == N-1:
        if gas > used + matrix[ci][cj]:
            gas = used + matrix[ci][cj]
        return

    if 0<= cj-1 < M and prev != 0:
        dfs(ci + 1, cj-1, used + matrix[ci][cj], 0)
    if 0<= cj+1 < M and prev != 1:
        dfs(ci + 1, cj+1, used + matrix[ci][cj], 1)
    if prev != 2:
        dfs(ci + 1, cj, used + matrix[ci][cj], 2)


# 3. M만큼 반복하며 시작한다 (시작지점 여러개로), 작은 값이 나올 때 마다 gas 소모량을 갱신
gas = 987654321

for start_point in range(M):
    dfs(0, start_point, 0, -1)
print(gas)
