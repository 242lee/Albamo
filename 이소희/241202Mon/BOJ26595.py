import sys
input = sys.stdin.readline

N = int(input())
A, Pa, B, Pb = map(int, input().split())

max_attack = 0
# (A*x) + (B*y) 가 최대가 되는
# x 탱커 수, y 딜러 수
max_x, max_y = 0, 0

# 고용 비용 Pa, + Pb <= N
for x in range(N//Pa + 1):
    money = N - (Pa * x)
    if money >= 0:
        y = money // Pb
        cur_attack = (A * x) + (B * y)
        if max_attack < cur_attack:
            max_attack = cur_attack
            max_x, max_y = x, y
print(max_x, max_y)