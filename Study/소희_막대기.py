'''
막대기를 반으로 잘라 32 32
여기서 X보다 크면 또 잘라 16 16 32

'''
N = int(input())
stick = 64
cnt = 0
while stick > 0:
    if stick > N:
        stick = stick // 2
    else:
        cnt += 1
        N -= stick
print(cnt)