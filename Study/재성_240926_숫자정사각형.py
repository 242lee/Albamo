import sys

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

side = min(N, M)
while side > 1:
    found = False
    for i in range(N - side + 1):
        ni = i + side - 1
        for j in range(M - side + 1):
            nj = j + side - 1
            if arr[i][j] == arr[ni][j] == arr[i][nj] == arr[ni][nj]:
                found = True
                break
        if found:
            break
    if found:
        break
    side -= 1

print(side**2)
