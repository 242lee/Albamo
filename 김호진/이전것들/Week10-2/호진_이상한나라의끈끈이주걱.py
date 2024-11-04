# 백준 32247 이상한 나라의 끈끈이주걱 실1
import sys
input = sys.stdin.readline

# 출구위치 N, 주걱개수 M
N, M = map(int, input().split())

trap = [list(map(int, input().split())) for _ in range(M)]
trap.sort(key=lambda x: x[1])

def escape():
    pre_x = pre_h = 0
    for c, x, h in trap:
        if c == 0:
            pre_h = max(h+1, pre_h - (x - pre_x))
            pre_x = x
        elif c == 1:
            if h-1 < pre_h - (x - pre_x):
                return 'adios'
            pre_h = pre_h - (x - pre_x)
            pre_x = x

    if 0 < pre_h - (N - pre_x):
        return 'adios'
    
    return 'stay'

print(escape())