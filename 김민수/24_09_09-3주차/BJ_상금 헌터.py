# 1차 대회 상금과 해당 등수 구간을 저장한 리스트
first_prize = [500, 300, 200, 50, 30, 10]

# first_prize_range는 해당 등수 구간을 나타냄. 
first_prize_range = [1, 2, 3, 4, 5, 6]

# 2차 대회 상금과 해당 등수 구간을 저장한 리스트
second_prize = [512, 256, 128, 64, 32]

# second_prize_range는 해당 등수 구간을 나타냄.
second_prize_range = [1, 2, 4, 8, 16]

# 1차 대회의 상금을 계산하는 함수
# 입력된 등수(rank)를 받아 그에 맞는 상금을 반환한다.
# 만약 등수가 0이거나 대회 범위를 벗어날 경우 상금은 0을 반환한다.
def get_first_prize(rank):
    if rank == 0 or rank > sum(first_prize_range):
        return 0  # 등수가 0이거나 범위를 벗어난 경우 상금은 0
    cumulative = 0  # 누적 등수를 계산하기 위한 변수
    for i in range(len(first_prize_range)):
        cumulative += first_prize_range[i]  # 구간을 하나씩 더해가며 등수 범위를 체크
        if rank <= cumulative:  # 해당 구간에 속하는지 확인
            return first_prize[i]  # 속하면 해당 상금을 반환
    return 0  # 등수가 범위를 벗어난 경우

# 2차 대회의 상금을 계산하는 함수
# 입력된 등수(rank)를 받아 그에 맞는 상금을 반환한다.
# 만약 등수가 0이거나 대회 범위를 벗어날 경우 상금은 0을 반환한다.
def get_second_prize(rank):
    if rank == 0 or rank > sum(second_prize_range):
        return 0  # 등수가 0이거나 범위를 벗어난 경우 상금은 0
    cumulative = 0  # 누적 등수를 계산하기 위한 변수
    for i in range(len(second_prize_range)):
        cumulative += second_prize_range[i]  # 구간을 하나씩 더해가며 등수 범위를 체크
        if rank <= cumulative:  # 해당 구간에 속하는지 확인
            return second_prize[i]  # 속하면 해당 상금을 반환
    return 0  # 등수가 범위를 벗어난 경우

# 입력 처리
t = int(input())  # 테스트 케이스의 수를 입력받음

# 테스트 케이스마다 1차 대회 등수와 2차 대회 등수를 입력받아 상금을 계산
for _ in range(t):
    a, b = map(int, input().split())  # 1차 대회 등수(a)와 2차 대회 등수(b)를 입력받음
    total_prize = get_first_prize(a) + get_second_prize(b)  # 1차와 2차 대회의 상금을 합산
    print(total_prize * 10000)  # 상금이 만원 단위이므로 최종 상금을 출력할 때 10000을 곱해줌
