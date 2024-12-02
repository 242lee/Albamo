# 돈 = N
# A = 탱커 전투력, PA = 고용 비용, B = 딜러 전투력, PB = 고용 비용
# Ax + By가 최대가 되도록

import sys
input = sys.stdin.readline

Money = int(input())
tanker_power, tanker_cost, dealer_power, dealer_cost = map(int, input().split())

max_power, best_tanker, best_dealer = 0, 0, 0

# 딜러 수를 0부터 가능한 최대까지 반복
for tanker_count in range(Money // tanker_cost + 1):
    dealer_count = (Money - tanker_count * tanker_cost) // dealer_cost
    total_power = tanker_power * tanker_count + dealer_power * dealer_count

    # 최적의 결과 갱신
    if total_power > max_power:
        max_power = total_power
        best_tanker = tanker_count
        best_dealer = dealer_count

# 결과 출력
print(best_tanker, best_dealer)


# 시간복잡도가 커보여서 다른 풀이 모색
# =================시도 1================================
# tanker_power / tanker_cost > dealer_power / dealer_cost의 값 비교해서 가장 효율적인 것을 많이쓰는게 좋지 않을까?
# 오류 : 
# 15
# 13 10 7 6 일 때 효율이 탱커가 더 좋은데 딜러 둘을 차용해야 Ax + By 가 더 크다.
# 기각

# import sys
# input = sys.stdin.readline

# Money = int(input())
# tanker_power, tanker_cost, dealer_power, dealer_cost = map(int, input().split())

# max_power, best_tanker, best_dealer = 0, 0, 0

# # 비용 대비 효율 계산
# tanker_efficiency = tanker_power / tanker_cost
# dealer_efficiency = dealer_power / dealer_cost

# if tanker_efficiency > dealer_efficiency:
#     # 탱커가 더 효율적일 때
#     max_tanker = Money // tanker_cost
#     remaining_money = Money % tanker_cost
#     best_tanker = max_tanker
#     best_dealer = remaining_money // dealer_cost
# elif dealer_efficiency > tanker_efficiency:
#     # 딜러가 더 효율적일 때
#     max_dealer = Money // dealer_cost
#     remaining_money = Money % dealer_cost
#     best_dealer = max_dealer
#     best_tanker = remaining_money // tanker_cost
# else:
#     # 효율이 같을 때 (탱커와 딜러를 조합하여 최적화)
#     for tanker_count in range(Money // tanker_cost + 1):
#         dealer_count = (Money - tanker_count * tanker_cost) // dealer_cost
#         total_power = tanker_power * tanker_count + dealer_power * dealer_count
#         if total_power > max_power:
#             max_power = total_power
#             best_tanker = tanker_count
#             best_dealer = dealer_count

# # 결과 출력
# print(best_tanker, best_dealer)