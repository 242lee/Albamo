# 시간 초과 ㅜ

def can_escape(N, M, traps):
    traps.sort()
    
    current_y = 0  
    previous_x = 0  

    # 각 끈끈이주걱에 대해 반복
    for i in range(M):
        c_i, x_i, h_i = traps[i]
        distance = x_i - previous_x

        if distance > 1:
            current_y = max(current_y - (distance - 1), h_i + 1)

        # 현재 위치에서 끈끈이주걱의 높이에 따라 피할 수 있는지 체크
        if c_i == 0:
            if current_y <= h_i:  # 현재 y좌표가 끈끈이주걱보다 작거나 같으면 실패
                return "adios"
        else:  # 위에서 내려온 경우
            if current_y >= h_i:  # 현재 y좌표가 끈끈이주걱보다 크면 실패
                return "adios"
        
        # 현재 끈끈이주걱의 x좌표를 이전 x좌표로 업데이트
        previous_x = x_i

    if previous_x == N and current_y == 0:
        return "stay"
    else:
        return "adios"

N, M = map(int, input().split())
traps = []

for _ in range(M):
    c_i, x_i, h_i = map(int, input().split())
    traps.append((c_i, x_i, h_i))

# 결과 출력
result = can_escape(N, M, traps)
print(result)
