"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49

35
"""
import heapq

n = int(input())
min_heap = []
num_list = [list(map(int, input().split())) for _ in range(n)]

# 2차원 리스트를 1차원 리스트로 변환
flat_list = [num for row in num_list for num in row]
flat_list.sort(reverse=True)
print(flat_list[n-1])
