# SK ; 상근, CY ; 창영, 상근선
# 1 or 3

# 1+1 = 2, 1 + 3 and 3 + 1 = 4, 3 + 3 = 6
# 2,4,6의 배수와 관련?

N = int(input())

# N을 분해하는 과정
a = N//6
a1 = N%6
b = a1//4
b1 = a1%4
c = b1//2
d = b1%2
if d == 0:
    print('CY')
else:
    print('SK')
