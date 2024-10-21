import sys
import heapq

input = sys.stdin.readline
N = int(input()) 
heap = []

for _ in range(N):
    a = int(input().strip())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heapq.heappop(heap)[1]) 
        else:
            print(0) 