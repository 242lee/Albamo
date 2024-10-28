# 마법의 나침반
'''
1번 방향: 보물은 x좌표가 작고, y좌표가 같은 곳에 있습니다.
2번 방향: 보물은 x좌표가 작고, y좌표가 큰 곳에 있습니다.
3번 방향: 보물은 x좌표가 같고, y좌표가 큰 곳에 있습니다.
4번 방향: 보물은 x좌표가 크고, y좌표가 큰 곳에 있습니다.
5번 방향: 보물은 x좌표가 크고, y좌표가 같은 곳에 있습니다.
6번 방향: 보물은 x좌표가 크고, y좌표가 작은 곳에 있습니다.
7번 방향: 보물은 x좌표가 같고, y좌표가 작은 곳에 있습니다.
8번 방향: 보물은 x좌표가 작고, y좌표가 작은 곳에 있습니다.
'''
# 마법의 나침반

N, M = map(int, input().split())
treasure_i, treasure_j = -1, -1  # 초기값을 임의로 설정

for _ in range(M):
    X, Y, K = map(int, input().split())

    if K == 1:                  # 보물은 x좌표가 작고, y좌표가 같은 곳
        if treasure_j == -1:
            treasure_j = Y
        treasure_i = min(treasure_i, X - 1) if treasure_i != -1 else X - 1
    elif K == 2:                # 보물은 x좌표가 작고, y좌표가 큰 곳
        treasure_i = min(treasure_i, X - 1) if treasure_i != -1 else X - 1
        treasure_j = max(treasure_j, Y + 1) if treasure_j != -1 else Y + 1
    elif K == 3:                # 보물은 x좌표가 같고, y좌표가 큰 곳
        treasure_i = X
        treasure_j = max(treasure_j, Y + 1) if treasure_j != -1 else Y + 1
    elif K == 4:                # 보물은 x좌표가 크고, y좌표가 큰 곳
        treasure_i = max(treasure_i, X + 1) if treasure_i != -1 else X + 1
        treasure_j = max(treasure_j, Y + 1) if treasure_j != -1 else Y + 1
    elif K == 5:                # 보물은 x좌표가 크고, y좌표가 같은 곳
        if treasure_j == -1:
            treasure_j = Y
        treasure_i = max(treasure_i, X + 1) if treasure_i != -1 else X + 1
    elif K == 6:                # 보물은 x좌표가 크고, y좌표가 작은 곳
        treasure_i = max(treasure_i, X + 1) if treasure_i != -1 else X + 1
        treasure_j = min(treasure_j, Y - 1) if treasure_j != -1 else Y - 1
    elif K == 7:                # 보물은 x좌표가 같고, y좌표가 작은 곳
        treasure_i = X
        treasure_j = min(treasure_j, Y - 1) if treasure_j != -1 else Y - 1
    elif K == 8:                # 보물은 x좌표가 작고, y좌표가 작은 곳
        treasure_i = min(treasure_i, X - 1) if treasure_i != -1 else X - 1
        treasure_j = min(treasure_j, Y - 1) if treasure_j != -1 else Y - 1


if 0 <= treasure_i <= N and 0 <= treasure_j <= N:
    print(treasure_i, treasure_j)

