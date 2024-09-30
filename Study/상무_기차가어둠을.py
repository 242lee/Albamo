'''
1. & (AND)
비교하는 비트가 둘 다 참일 때 만족
0011 & 0110 = 0010
2. | (OR)
비교 하는 비트 둘 중 하나라도 참이면 만족
0011 | 0110 = 0111
3. ^ (XOR)
비교 하는 비트가 서로 달라야 만족
0011 ^ 0110 = 0101
4. ~ (NOT)
보수 연산 0->1, 1->0
a가 0011일 때, ~a는 1100
5. << (왼쪽 shift)
특정 값 n만큼 왼쪽으로 비트 이동
a가 0011일 때, a << 2는 1100
2^n를 곱한만큼 값이 증가
6. >> (오른쪽 shift)
특정 값 n만큼 오른쪽으로 비트 이동
a가 0110일 때, a << 1는 0011
2^n을 나눈만큼 값이 감소
'''
# 문제를 손으로 풀다보니까 대놓고 비트연산으로 풀라고 돼있다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trains = [0] * (N + 1)

for _ in range(M):
    # 값이 2개, 3개 각각 다르므로 t랑 i는 무조건 값을 받아오는데 나머지 값을 받아오기 위해서 *x로 받아온다.
    command, i, *x = map(int, input().split())
    
    if command == 1:
        trains[i] |= (1 << (x[0] - 1))  # i번째 열차 x번째 비트 1로 만들기
    elif command == 2:
        trains[i] &= ~(1 << (x[0] - 1))  # i번째 열차 x번째 비트 0으로 만들기
    elif command == 3:
        trains[i] &= ~(1 << 19)  # i번째 열차 가장 왼쪽 비트 0으로 만들기
        trains[i] <<= 1  # 각 비트 왼쪽으로 SHIFT
    else:
        trains[i] &= ~1  # i번째 열차 가장 오른쪽 비트 0으로 만들기
        trains[i] >>= 1  # 각 비트 오른쪽으로 SHIFT

result = set(trains[1:])  # 중복 제거하여 기차 저장

print(len(result))  # 기차의 개수 출력
