from itertools import permutations

def solution(n, weak, dist):
    # weak 배열을 두 번 이어 붙여서 원형을 일자 형태로 처리
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 친구를 최소한으로 투입하기 위한 값
    answer = len(dist) + 1  # dist의 최대 길이가 8이므로, 모든 친구를 다 사용해도 안 될 경우를 위해 설정
    
    # 친구를 배치할 수 있는 모든 경우의 수 탐색
    for start in range(length):
        # 친구 순열로 경우의 수를 모두 시도
        for friends in permutations(dist):
            count = 1  # 투입할 친구 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 현재 점검 위치를 넘어서면 다음 친구 투입
                if position < weak[index]:
                    count += 1  # 다음 친구 투입
                    if count > len(dist):  # 친구를 모두 사용했으면 중단
                        break
                    # 다음 친구가 점검할 수 있는 최대 위치 갱신
                    position = weak[index] + friends[count - 1]
            
            # 최소 친구 수 갱신
            answer = min(answer, count)
    
    # 모든 친구를 투입해도 안 되면 -1을 반환
    if answer > len(dist):
        return -1
    
    return answer
