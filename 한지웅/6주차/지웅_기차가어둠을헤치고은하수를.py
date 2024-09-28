# Rule
# 1. 1 i x : i (1~N) 기차 x 좌석 사람 태우기, 사람이 타있다면 무시
# 2. 2 i x : i 기차 x 좌석 하차, 아무도 없다면 무시
# 3. 3 i : i번째 기차 승객 모두 한칸씩 뒤로, 20번째 승객은 하차
# 4. 4 i : 모두 한칸씩 앞으로, 1번째 자리 사람은 하차

# deque의 rotate활용

from collections import deque

# 1번 명령 (탑승)
def ord_one(ord_data):
    global train_info
    target_train = ord_data[1]
    target_seat = ord_data[2]
    if train_info[target_train - 1][target_seat - 1] == 0:
        train_info[target_train - 1][target_seat - 1] = 1
    return
# 2번 명령 (내려)
def ord_two(ord_data):
    global train_info
    target_train = ord_data[1]
    target_seat = ord_data[2]
    if train_info[target_train - 1][target_seat - 1] == 1:
        train_info[target_train - 1][target_seat - 1] = 0
    return
# 3번 명령 (뒤로)
def ord_three(ord_data):
    global train_info
    target_train = ord_data[1]
    if train_info[target_train - 1][19] == 1:
        train_info[target_train - 1][19] = 0
    train_info[target_train - 1].rotate(1)
    return
# 4번 명령 (앞으로)
def ord_four(ord_data):
    global train_info
    target_train = ord_data[1]
    if train_info[target_train - 1][0] == 1:
        train_info[target_train - 1][0] = 0
    train_info[target_train - 1].rotate(-1)
    return

# ord를 수행하는 함수, ord number에 따라 적합한 명령 수행
def ord_funnel(ord_data):
    numb = ord_data[0]
    if numb == 1:
        ord_one(ord_data)
        return
    elif numb == 2:
        ord_two(ord_data)
        return
    elif numb == 3:
        ord_three(ord_data)
        return
    else:
        ord_four(ord_data)
        return

# 기차의 수 N, 명령의 수 M
N, M = map(int, input().split())
train_info = [deque([0 for _ in range(20)]) for _ in range(N)]
for _ in range(M):
    ord = list(map(int,input().split()))
    ord_funnel(ord)

# set을 활용하여 중복 제거
check = set()
for _ in range(N):
    check.add(tuple(train_info[_]))

print(len(check))
