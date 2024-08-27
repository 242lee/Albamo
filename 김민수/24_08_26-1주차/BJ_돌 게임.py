"""
돌 게임은 두 명이서 즐기는 재밌는 게임이다.
탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

완벽하게란 최대한 적은 횟수로 게임을 끝낸다는 것
3을 나눈 나머지가 0이고 몫이 홀수면 SK / 짝수면 CY
3을 나눈 나머지가 있고 몫이 홀수이고 나머지가 홀수면 CY 짝수면 SK
3을 나눈 나머지가 있고 몫이 짝수이고 나머지가 홀수면 SK 짝수면 CY

나누기를 할 때 몫과 나머지를 동시에 구할 수 있는 내장 함수인 divmod()
"""

def is_even(number):
    return number % 2 == 0  # 짝수면 True, 홀수면 False 반환


N = int(input())

winner = ''

division_result = divmod(N, 3)
# 3을 나눈 나머지가 0이고 몫이 홀수면 SK / 짝수면 CY
if division_result[1] == 0:
    if is_even(division_result[0]):
        winner = 'CY'
    else:
        winner = 'SK'

# 나머지가 있는 경우
else:
    # 3을 나눈 나머지가 있고 몫이 짝수인 경우 나머지가 홀수면 SK 짝수면 CY
    if is_even(division_result[0]):
        if is_even(division_result[1]):
            winner = 'CY'
        else:
            winner = 'SK'

    # 3을 나눈 나머지가 있고 몫이 홀수이고 나머지가 홀수면 CY 짝수면 SK
    if is_even(division_result[0]) == False:
        if is_even(division_result[1]):
            winner = 'SK'
        else:
            winner = 'CY'

print(winner)