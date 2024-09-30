n, m = map(int, input().split())
trains = [0] * n  # 기차 상태를 비트마스크로 관리

for _ in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        # 1 i x: i번째 기차의 x번째 자리에 사람을 태운다
        trains[command[1] - 1] |= (1 << (command[2] - 1))
    elif command[0] == 2:
        # 2 i x: i번째 기차의 x번째 자리에서 사람을 내린다
        trains[command[1] - 1] &= ~(1 << (command[2] - 1))
    elif command[0] == 3:
        # 3 i: i번째 기차의 모든 사람이 한 칸 뒤로 이동한다
        trains[command[1] - 1] = (trains[command[1] - 1] << 1) & ((1 << 20) - 1)
    elif command[0] == 4:
        # 4 i: i번째 기차의 모든 사람이 한 칸 앞으로 이동한다
        trains[command[1] - 1] >>= 1

# 기차 상태의 중복을 없애기 위해 set 사용
unique_trains = set(trains)
print(len(unique_trains))
