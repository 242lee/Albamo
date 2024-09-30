# 지피티가 풀어줌용

N, M = map(int, input().split())
trains = [0] * (N + 1)  # 각 열차의 좌석 상태를 20비트로 관리

for _ in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1:  # 1번 명령: 해당 좌석에 사람을 태움
        train_id = command[1]
        seat = command[2] - 1  # 좌석 번호를 0부터 시작하게 맞춤
        trains[train_id] |= (1 << seat)
    
    elif command[0] == 2:  # 2번 명령: 해당 좌석에서 사람을 내림
        train_id = command[1]
        seat = command[2] - 1
        trains[train_id] &= ~(1 << seat)
    
    elif command[0] == 3:  # 3번 명령: 모든 사람을 한 칸 뒤로 이동
        train_id = command[1]
        trains[train_id] = (trains[train_id] << 1) & ((1 << 20) - 1)  # 20비트를 넘지 않도록 마스크
    
    elif command[0] == 4:  # 4번 명령: 모든 사람을 한 칸 앞으로 이동
        train_id = command[1]
        trains[train_id] >>= 1

# 중복되지 않은 열차 상태 세기
unique_trains = set(trains[1:])  # 첫 번째 열차부터 마지막 열차까지 고유한 상태만 저장
print(len(unique_trains))
