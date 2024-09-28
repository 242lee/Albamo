# 백준 15787 기차가 어둠을 헤치고 은하수를 실2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [[0] * 22 for _ in range(N+1)]

for m in range(M):
    command, i, *x = map(int, input().split())

    if command == 1:
        train[i][x[0]] = 1

    elif command == 2:
        train[i][x[0]] = 0

    elif command == 3:
        for j in range(20, 0, -1):
            train[i][j] = train[i][j-1]

    elif command == 4:
        for j in range(1, 21):
            train[i][j] = train[i][j+1]

passed = []
for i in range(1, N+1):
    if train[i] not in passed:
        passed.append(train[i])

print(len(passed))
