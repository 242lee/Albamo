import sys
input = sys.stdin.readline

def count_ones_in_binary(N):
    # N을 2진수로 변환하고, '1'의 개수를 세기
    return bin(N).count('1')

print(count_ones_in_binary(int(input())))