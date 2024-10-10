from heapq import heappush, heappop
import sys

input = sys.stdin.readline

X = int(input())
h = [64]
while sum(h) > X:
    short = heappop(h)
    half = short // 2
    heappush(h, half)
    if sum(h) < X:
        heappush(h, half)

print(len(h))
