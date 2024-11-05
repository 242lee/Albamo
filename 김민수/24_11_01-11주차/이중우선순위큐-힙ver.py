import heapq

def solution(operations):
    min_heap = []  # 최소 힙을 통해 최솟값을 추적
    max_heap = []  # 최대 힙을 통해 최댓값을 추적
    entry_finder = {}  # 삽입된 항목을 추적해 삭제된 항목을 관리
    
    for operation in operations:
        op, val = operation.split()
        val = int(val)
        
        if op == "I":
            # 값을 최소 힙과 최대 힙에 추가
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            entry_finder[val] = entry_finder.get(val, 0) + 1
        elif op == "D":
            if val == 1 and max_heap:
                # 최대 힙에서 삭제
                while max_heap:
                    max_value = -heapq.heappop(max_heap)
                    if entry_finder.get(max_value, 0) > 0:
                        entry_finder[max_value] -= 1
                        break
            elif val == -1 and min_heap:
                # 최소 힙에서 삭제
                while min_heap:
                    min_value = heapq.heappop(min_heap)
                    if entry_finder.get(min_value, 0) > 0:
                        entry_finder[min_value] -= 1
                        break
    
    # 결과를 계산
    while min_heap and entry_finder.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
        
    while max_heap and entry_finder.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
