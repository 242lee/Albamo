# 효율성 통과 못함
'''
정확성: 83.9
효율성: 0.0
합계: 83.9 / 100.0
'''

def solution(scoville, K):
    answer = 0
    
    while len(scoville) > 1: 
        scoville.sort() 
        if scoville[0] >= K: 
            return answer
        new_scoville = scoville[0] + scoville[1] * 2
        scoville = [new_scoville] + scoville[2:]
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer


'''
# 효율성까지 통과
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville) 
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville) 
        answer += 1

    return answer

'''