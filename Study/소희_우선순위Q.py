from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    valid_entries = set() 

    for operation in operations:
        order, num = operation.split()
        num = int(num)

        if order == 'I':  # 숫자 삽입
            heappush(min_heap, num)
            heappush(max_heap, -num)
            valid_entries.add(num)
        elif order == 'D':  # 삭제 명령어
            if valid_entries:
                if num == 1:  # 최댓값 삭제
                    while max_heap and -max_heap[0] not in valid_entries:
                        heappop(max_heap)
                    if max_heap:
                        max_val = -heappop(max_heap)
                        valid_entries.remove(max_val)
                elif num == -1:  # 최솟값 삭제
                    while min_heap and min_heap[0] not in valid_entries:
                        heappop(min_heap)
                    if min_heap:
                        min_val = heappop(min_heap)
                        valid_entries.remove(min_val)

    if not valid_entries:
        return [0, 0]
    else:
        while min_heap and min_heap[0] not in valid_entries:
            heappop(min_heap)
        while max_heap and -max_heap[0] not in valid_entries:
            heappop(max_heap)
        min_val = min_heap[0]
        max_val = -max_heap[0]
        return [max_val, min_val]
