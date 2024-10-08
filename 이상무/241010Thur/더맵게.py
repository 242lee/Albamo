import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    # 가장 작은 값이 K 이상이 될 때까지 반복
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1  # 모든 음식을 K 이상으로 만들 수 없을 경우 -1 반환

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))