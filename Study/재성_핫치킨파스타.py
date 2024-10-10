from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b*2)
        answer += 1
        
    if scoville[0] < K:
        return -1
    else:
        return answer
