'''
기차번호 1 ~ N
기차하나당 M개의 명령
1. i번 기차의 x번 자리에 태워. 이미 있으면 nothing
2. i번 기차 x번 자리 내려. 없으면 nothing
3. i번 기차 모두 한칸씩 뒤로 가. 맨 뒷자리 사람은 내려
4. i번 기차 모두 한칸씩 앞으로. 맨 앞자리 사람은 내려
'''

# 80%에서 실패함 아무나 디버깅 좀 >..<
N, M = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(M)]

trains = [[0] * 20 for _ in range(N + 1)]

for order in orders:
    train_id = order[1] - 1 
    if order[0] == 1:  # 1번 명령
        seat = order[2] - 1
        trains[train_id][seat] = 1
    elif order[0] == 2:  # 2번 명령
        seat = order[2] - 1
        trains[train_id][seat] = 0
    elif order[0] == 3:  # 3번 명령
        for i in range(19, 0, -1):
            trains[train_id][i] = trains[train_id][i-1]
        trains[train_id][0] = 0  
    elif order[0] == 4:  # 4번 명령
        for i in range(19):
            trains[train_id][i] = trains[train_id][i+1]
        trains[train_id][19] = 0 

passTrain = set()
for train in trains:
    # print(tuple(train))
    passTrain.add(tuple(train))

print(len(passTrain))