'''
이렇게 단순하게 푸는 게 맞나 싶어서 한참 고민함
근데 그래도 됐던 것
'''

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    reward = 0

    # 1회 상금
    if a == 0:
        pass
    elif a <= 1:
        reward += 500
    elif a <= 3:
        reward += 300
    elif a <= 6:
        reward += 200
    elif a <= 10:
        reward += 50
    elif a <= 15:
        reward += 30
    elif a <= 21:
        reward += 10

    # 2회 상금
    if b == 0:
        pass
    elif b <= 1:
        reward += 512
    elif b <= 3:
        reward += 256
    elif b <= 7:
        reward += 128
    elif b <= 15:
        reward += 64
    elif b <= 31:
        reward += 32

    print(reward*10000)