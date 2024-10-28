from itertools import permutations

def solution(n, weak, dist):
    weakLen = len(weak)
    weak = weak + [num + n for num in weak]     # 원형으로
    minCnt = float('inf')  
    dist = [0] + dist                           # 친구들의 거리 앞에 0을 추가
    
    for start in range(weakLen):
        for friends in permutations(dist[1:]):  # dist에서 permutations 생성
            cnt = 1
            idx = start
            for i in range(1, weakLen):
                nextidx = start + i
                dis = weak[nextidx] - weak[idx]
                if dis > friends[cnt - 1]:      # 친구가 커버할 수 없는 경우
                    idx = nextidx
                    cnt += 1
                    if cnt > len(friends):
                        break
            if cnt <= len(friends):
                minCnt = min(minCnt, cnt)
        
    # minCnt가 `inf` 그대로 있는 경우 -1 반환
    if minCnt == float('inf'):
        return -1
    return minCnt
