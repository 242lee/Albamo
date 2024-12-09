# 백준 26595 전투의 신 실버5
import sys
input = sys.stdin.readline

N = int(input())
A, Pa, B, Pb = map(int, input().split())

max_power = 0
max_x, max_y = 0, 0

for x in range(N // Pa + 1):
    y = (N - x * Pa) // Pb
    if y >= 0:
        power = A * x + B * y
        if power > max_power:
            max_power = power
            max_x, max_y = x, y

print(max_x, max_y)