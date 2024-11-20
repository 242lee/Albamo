# 백준 13335 트럭 실버1
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

q = [0] * w
idx = 0

ss = 0
sec = 0
i = 0
while i < n:
    sec += 1
    t = trucks[i]
    if q[idx] != 0:
        ss -= q[idx]
        q[idx] = 0
    if ss + t <= L:
        ss += t
        q[idx] = t
        i += 1
    idx = (idx + 1) % w

print(sec + w)