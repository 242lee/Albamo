'''
x = 1, y = 5 인 경우
1) 속도 1, 거리 1 이동 (현재 위치: 2)
2) 속도 2, 거리 2 이동 (현재 위치: 4)
3) 속도 1, 거리 1 이동 (현재 위치: 5)
'''
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x

    step = 0
    if d == 1:
        step = 1
    elif d == 2:
        step = 2
    else:
        # 가운데 찾기
        n = 1
        while n * n <= d:
            n += 1
        n -= 1

        if d == n * n:  # 대칭 이동
            step = 2 * n - 1
        elif n * n < d <= n * n + n:
            step = 2 * n
        else:
            step = 2 * n + 1
    print(step)