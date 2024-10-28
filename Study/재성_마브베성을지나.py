import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

compasses = {
    1: (-1, 0),
    2: (-1, 1),
    3: (0, 1),
    4: (1, 1),
    5: (1, 0),
    6: (1, -1),
    7: (0, -1),
    8: (-1, -1)
}

target = [[1, N], [1, N]]
flags = [False, False]

cnt = 0
for cmd in range(M):
    cnt += 1
    tmp = list(map(int, input().split()))
    tmp_c = compasses[tmp[2]]
    for idx in range(2):
        if flags[idx]:
            continue

        if tmp_c[idx] == 1:
            if target[idx][0] < tmp[idx] + 1:
                target[idx][0] = tmp[idx] + 1

        elif tmp_c[idx] == -1:
            if target[idx][1] > tmp[idx] - 1:
                target[idx][1] = tmp[idx] - 1

        else:
            target[idx] = [tmp[idx], tmp[idx]]
            flags[idx] = True


print(target[0][0], target[1][0])
