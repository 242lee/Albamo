import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = {}

    for operation in operations:
        command, num = operation.split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            visited[num] = visited.get(num, 0) + 1

        elif command == "D":
            if num == 1:
                # 최대 힙에서 유효한 값이 나올 때까지 반복
                while max_heap and not visited.get(-max_heap[0], 0):
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    visited[max_val] -= 1
                    if visited[max_val] == 0:
                        del visited[max_val]

            elif num == -1:
                while min_heap and not visited.get(min_heap[0], 0):
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    visited[min_val] -= 1
                    if visited[min_val] == 0:
                        del visited[min_val]

    # 유효한 값만 남기기
    while min_heap and not visited.get(min_heap[0], 0):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(-max_heap[0], 0):
        heapq.heappop(max_heap)

    # 결과 반환
    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
