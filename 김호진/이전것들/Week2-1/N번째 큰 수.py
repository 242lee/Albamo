# 백준 2075 N번째 큰 수 실2

import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
h.sort()

for _ in range(1, n):
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, arr[i])

print(h[0])

# deque로 heapq처럼 구현했는데 시간초과. 이유는 모름. 알면 공유점

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# dq = deque(arr)

# for _ in range(1, n):
#     arr = list(map(int, input().split()))
#     for i in range(n):
#         for j in range(n):
#             if arr[i] < dq[j]:
#                 dq.insert(j, arr[i])
#                 dq.popleft()
#                 break
#         else:
#             dq.append(arr[i])
#             dq.popleft()

# print(dq[0])