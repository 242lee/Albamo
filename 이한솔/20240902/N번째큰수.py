'''
n번째로 큰 수
메모리 초과 이슈로 힙의 크기를 n으로 유지하는 것이 중요
힙 첨 써봄

최소 힙 (min-heap) 이론

이진트리 기반의 자료구조, 최소힙으로 구현

- 힙 (heap) : 각 노드가 자식 노드보다 항상 크거나 작도록 유지되는 자료구조
- 최소힙 (min-heap) : 최소 힙의 루트노드는 항상 가장 작은 값

- heappush(heap, item) : 힙에 item 추가 후 힙의 특성이 유지되도록 트리 구조 재정렬
- heappop(heap) : 힙에서 가장 작은 요소를 제거하고 반환 
'''

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n): # n 줄이므로 n번 반복
    nums = list(map(int, sys.stdin.readline().split()))
    # 숫자들 받아


    # heap에 아무것도 없으면 heap에 추가해
    # 즉 heap의 크기가 n을 유지하게 됨
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    
    # heap이 이미 있으면
    # heap의 가장 앞의 수와 비교해서 더 크면 넣어
    else: 
        for num in nums:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

# heap의 크기가 n이므로 n번째로 큰 수는 0번째 인덱스
print(heap[0])