# f(x) = n * (n+1) / 2
# n^2 + n - 2f(x) = 0
# n = ( -1 + sqrt(1 + 8n) ) / 2
import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    first_rank, second_rank = map(int, input().split())
    first_prize_list = [0, 5000000, 3000000, 2000000, 500000, 300000, 100000]
    if 0 < first_rank < 22:
        first_num = int(math.ceil( -1 + math.sqrt(1 + 8 * first_rank)) / 2)
        first_prize = first_prize_list[first_num]
    else:
        first_prize = 0
    if 0 < second_rank < 32:
        second_num = math.ceil(math.log2(second_rank + 1))
        second_prize = 10 ** 4 * 2 ** (10 - second_num)
    else:
        second_prize = 0

    print(first_prize + second_prize)

# 왜 틀린지 모르겠음