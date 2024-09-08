# 백준 15953 상금 헌터 브3

import sys
input = sys.stdin.readline

T = int(input())
prize1 = [0, 500] + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6 + [0] * 79
prize2 = [0, 512] + [256]*2 + [128]*4 + [64]*8 + [32]*16 + [0] * 33
for _ in range(T):
    a, b = map(int, input().split())
    print((prize1[a] + prize2[b]) * 10000)
