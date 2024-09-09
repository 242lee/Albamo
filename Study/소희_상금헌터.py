T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    reward = 0

    # 1회 상금계산
    if a == 0:
        reward += 0
    elif a == 1:
        reward += 500
    elif a <= 1 + 2:
        reward += 300
    elif a <= 1 + 2 + 3:
        reward += 200
    elif a <= 1 + 2 + 3 + 4:
        reward += 50
    elif a <=  1 + 2 + 3 + 4 + 5:
        reward += 30
    elif a <=  1 + 2 + 3 + 4 + 5 + 6:
        reward += 10

    # 2회 상금계산
    if b == 0:
        reward += 0
    elif b == 1:
        reward += 512
    elif b <= 1 + 2:
        reward += 256
    elif b <= 1 + 2 + 4:
        reward += 128
    elif b <= 1 + 2 + 4 + 8:
        reward += 64
    elif b <= 1 + 2 + 4 + 8 + 16:
        reward += 32

    print(reward*10000)