'''
메모리 31252KB 시간 36ms
'''

N = int(input())

# 홀수면 상근이가 이기고, 짝수면 창영이가 이기는 건가
if N % 2 == 1:
    print('SK')
else:
    print('CY')