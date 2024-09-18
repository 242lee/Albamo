from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    tan_cnt = 0
    
    size = defaultdict(int)
    for tan in tangerine:
        size[tan] += 1
    sorted_dict = sorted(size.items(), key= lambda item:item[1], reverse=True)
    # print(sorted_dict)
    
    for size, cnt in sorted_dict:
        if tan_cnt < k:
            tan_cnt += cnt
            answer += 1
            
    return answer