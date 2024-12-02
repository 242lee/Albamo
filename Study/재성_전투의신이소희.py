import sys
input = sys.stdin.readline

N = int(input())
A, Pa, B, Pb = map(int, input().split())

# 최적의 결과를 저장할 변수
max_power = 0
best_x, best_y = 0, 0

# 가능한 탱커의 고용 수를 순회
for x in range(N // Pa + 1):  # 탱커를 고용할 수 있는 최대 수
    remaining_money = N - x * Pa  # 남은 예산
    y = remaining_money // Pb  # 남은 예산으로 고용 가능한 딜러 수
    current_power = A * x + B * y  # 현재 조합의 전투력

    if current_power > max_power:  # 전투력이 더 높으면 업데이트
        max_power = current_power
        best_x, best_y = x, y

print(best_x, best_y)
