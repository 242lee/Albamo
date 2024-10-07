# def count_ones(n):

#     return bin(n).count('1')

# def range_ones(A, B):
#     total_count = 0
    
#     for x in range(A, B + 1):
#         total_count += count_ones(x)
        
#     return total_count

# A, B = map(int, input().split())

# result = range_ones(A, B)
# print(result)
# 시간초과...

import sys
import math

input = sys.stdin.readline

def count_ones_in_power_range(x):
    # 종료 조건: x가 0일 때
    if x == 0:
        return 1

    count = 2 ** x + x * (2 ** (x - 1))
    
    # 재귀 호출하여 x-1에 대한 1의 개수를 더함
    return count + count_ones_in_power_range(x - 1)

def count_total_ones(n):
    result = 0
    
    while n > 0:
        log2n = int(math.log2(n))  # log2n의 정수값을 구함
        # print(log2n)
        result += count_ones_in_power_range(log2n)  # 1의 개수 계산
        n -= 2 ** log2n
        result += n

    return result

# 입력값 A와 B
A, B = map(int, input().split())

# A에서 B까지의 1의 개수를 세기 위해 B의 1의 개수에서 A-1의 1의 개수를 빼줌
result = count_total_ones(B) - count_total_ones(A - 1)

# print(result)
print(count_total_ones(4))
