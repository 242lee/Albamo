import sys
input = sys.stdin.readline

# 2 <= N <= 20, 1 <= M <= 3
N, M = map(int, input().split())
# 1 <= trees[i][j] <= 1000
trees = [list(map(int, input().split())) for _ in range(N)]
friends = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 친구 M명의 각 시간별 동선 체크용 visited 생성
v = [[[-1] * M for _ in range(N)] for _ in range(N)]

# 0초 수확
ss = 0
for i in range(len(friends)):
    fi = friends[i][0] - 1
    fj = friends[i][1] - 1
    ss += trees[fi][fj]
    v[fi][fj][i] = 0
max_ss = ss

def dfs(i, j, m, sec):
    global max_ss, ss
    # 3초 다 수확하면
    if sec == 3:
        # 다음 친구의 DFS 시작
        if m+1 < M:
            dfs(friends[m+1][0]-1, friends[m+1][1]-1, m+1, 0)
            return
        # M번째 친구까지 다 탐색하면 최대 수확량 산출
        else:
            max_ss = max(max_ss, ss)
            return
    
    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]

        # 다음 이동이 다른 친구와 겹치지 않으면 이동
        if (0 <= ni < N) and (0 <= nj < N) and (sec+1 not in v[ni][nj]):
            
            # 처음 수확하는 경우에만 수확
            if v[ni][nj] == [-1] * M:
                v[ni][nj][m] = sec+1
                ss += trees[ni][nj]
                dfs(ni, nj, m, sec+1)
                ss -= trees[ni][nj]
                v[ni][nj][m] = -1
            else:
                # 시간을 덮어쓰는 경우를 대비해 tmp에 이전 시간 저장
                tmp, v[ni][nj][m] = v[ni][nj][m], sec+1
                dfs(ni, nj, m, sec+1)
                v[ni][nj][m] = tmp


# m번째 친구의 1~3초 수확
dfs(friends[0][0]-1, friends[0][1]-1, m=0, sec=0)
print(max_ss)
