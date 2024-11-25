def solution(targets):
    # 1. 끝점 기준 정렬
    targets.sort(key=lambda x: x[1])
    
    count = 0                       # 요격 미사일의 수
    last_shot = float('-inf')       # 마지막으로 요격 미사일을 발사한 위치
    
    for start, end in targets:
        # 2. 현재 요격 미사일로 요격 불가능한 경우 새로 발사
        if last_shot < start:
            count += 1
            last_shot = end - 0.5   # end를 포함하지 않도록 조정
    
    return count
