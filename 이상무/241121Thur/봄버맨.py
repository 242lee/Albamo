# 폭탄은 3초 후 폭발
# 폭발한 이후 폭탄이 있던 칸 = 빈 칸, 인접한 네 칸(십자모양) = 빈 칸
# 폭발한 이후 인접한 네 칸 중 폭탄이 있다면 그 폭탄은 그냥 제거된다.

# 봄버맨
# 봄버맨은 일부 칸에 폭탄을 설치한다. 시작 시간은 같다.
# 다음 1초동안 봄버맨 아무 행동 column
# 다음 1초 동안 폭탄이 설치되지않은 모든 칸에 폭탄 설치. 폭탄은 모두 같은 시간에 설치했다고 가정
# 1초가 지난 후 3초 전에 설치된 폭탄이 모두 폭발한다.
# 3과 4를 반복한다.

# 0초 = initial state
# 1초 = 아무 행동 X
# 2초 = 폭탄이 설치되지않은 모든 칸에 폭탄 설치
# 3초 = 3초전에 설치한 폭탄 폭발
# 4초 = 폭탄이 설치되지 않은 모든 칸에 폭탄 설치
# 5초 = 3초전에 설치한 폭탄 폭발
# 6초 = 폭탄이 설치되지 않은 모든 칸에 폭탄 설치
# 7초 = 3초전에 설치한 폭탄 폭발

# [.O., 
#  OOO,
#  .O.]
# 위와 아래의 5초후 결과는 같다.
# [.O.,
#  O.O,
#  .O.]
# 즉 바둑과 같다고 볼 수 있다.
# 내가 폭탄이 아닐 때 내 주변이 벽과 폭탄으로 둘러쌓여있으면 폭탄으로 바뀐다.

import sys
input = sys.stdin.readline

R, C, time = map(int, input().split())
initial_bomb = [list(input().strip()) for _ in range(R)]

if time <= 1:
    for bombs in initial_bomb:
        print(''.join(bombs))
elif time %2 == 0:
    for i in range(R):
        print('O'*C)
else :
    first_bomb = [['O'] * C for _ in range(R)]
    for row in range(R):
        for column in range(C):
            if initial_bomb[row][column]=='O':
                first_bomb[row][column] = '.'
            else:
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if row + i >= 0 and row + i < R and column + j >= 0 and column + j < C and initial_bomb[row+i][column+j]=='O':
                        first_bomb[row][column] = '.'
                        break

    second_bomb = [['O'] * C for _ in range(R)]
    for row in range(R):
        for column in range(C):
            if first_bomb[row][column]=='O':
                second_bomb[row][column] = '.'
            else:
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if row + i >= 0 and row + i < R and column + j >= 0 and column + j < C and first_bomb[row+i][column+j]=='O':
                        second_bomb[row][column] = '.'
                        break

    if time % 4 == 3:
        for bombs in first_bomb:
            print(''.join(bombs))
    if time % 4 == 1:
        for bombs in second_bomb:
            print(''.join(bombs))


