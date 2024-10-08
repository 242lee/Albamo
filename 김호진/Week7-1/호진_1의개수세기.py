# 백준 9527 1의 개수 세기 골2
from itertools import combinations
import sys
input = sys.stdin.readline

# 1 ~ 10^16
A, B = map(int, input().split())

'''
1. 규칙 찾기
2^1 -> 1 : 1*1 = 1
2^2 -> 01, 10, 11 : 1*2 + 2*1 = 4
2^3 -> 001, 010, 100, 011, 101, 110, 111 : 1*3 + 2*3 + 3*1 = 12
2^n -> n개 중 1개 뽑는 경우의 수 + n개 중 2개 뽑는 경우의 수 + ... + n개 중 n개 뽑는 경우의 수
즉, 2^n 까지의 1의 개수 = nC1 + nC2 + ... + nCn-1 + nCn

2. 풀이 전략 수립
A부터 B까지의 1의 개수 = B까지의 1의 개수 - A-1까지의 1의 개수

3. 디테일
A와 B는 10진수이므로 2^n 승으로 딱 떨어지지 않음
x(10진수)까지의 1의 개수 구하는 법을 알아야함

(2^(k+1) > x > 2^k) -> x //= 2^k, cnt += 2^k까지의 개수
(2^(k'+1) > x > 2^k') -> x //= 2^k', cnt += 2^k'까지의 개수
x가 0이 될 때까지 반복

위처럼 하면 10진수를 2진수로 잘게 쪼개어 1의 개수를 셀 수 있을듯

4. 킥
x.bit_length()를 쓰면 x를 이진수로 표현하는 데 필요한 비트수(자릿수)를 구할 수 있음
'''


'''
def count_ones_up_to(x):
    print('x:', x)
    cnt = 0
    while x > 0:
        # 2^k+1 < x < 2^k
        k = x.bit_length() - 1
        print(f'now k={k} 2^k={2**k}')
        
        for a in range(1, k + 1):
            cnt += a * comb(k, a)  # 조합 nCk로 1의 개수를 계산
            print(cnt)
        
        # 남은 x 값에서 해당 비트 값을 빼고 계속 진행
        x -= 2**k

        print('next x:', x)
    return cnt

def ones_in_power_of_two(n):
    # 2^n까지의 1의 개수를 계산 (조합으로)
    count = 0
    for k in range(1, n + 1):
        count += comb(n, k)  # 조합 nCk로 1의 개수를 계산
    return count

def comb(n, k):
    # 조합 계산 (nCk)
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


result = count_ones_up_to(B) - count_ones_up_to(A - 1)
print(result)
'''
# 는 실패. 2^k승에 딱 떨어지지 않는 10진수를 처리할 때, 
# 1101 -> 101 -> 1 순으로 1의 개수를 세어 나가는데, 
# 101을 셀 때는 1000을, 1을 셀 때는 1100을 포함해서 세야하는 데 이 로직이 누락됨.
# 그리고 조합 계산 재귀함수쪽이 10^16정도를 커버하기엔, 코드 구현을 완벽히 해도 아마 시간초과 날듯


# 이번엔 다른 패턴을 분석해봄
'''
각 자릿수를 보면 패턴이 있음
4자릿수로 보면
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
0번째 자릿수는 0 1 ...
1번째 자릿수는 0 0 1 1 ...
2번째 자릿수는 0 0 0 0 1 1 1 1 ...
3번째 자릿수는 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 ...
즉, 각 자릿수가 몇 번 반복되는지를 파악하면 1의 갯수를 자릿수별로 쉽게 파악가능
각 반복되는 패턴을 블럭이라고 표현하겠음
예를들어 0번째 자릿수는 0 1 이 한 블럭
3번째 자릿수는 한 블럭의 길이가 16이고 1의 개수는 8개이므로 블럭의 길이 = 2^4, 1의 개수 = 2^3
즉, i번째 자릿수는 한 블럭의 길이가 2^(i+1), 1의 개수가 2^i
'''
def count_ones_up_to(x):
    cnt = 0  # 1의 개수를 저장할 변수
    bit_length = x.bit_length()  # x를 이진수로 표현하는 데 필요한 비트 수
    
    # 각 비트 위치(i)에 대해 1이 나타나는 빈도를 계산
    for i in range(bit_length):
        # i번째 자릿수(2^i)가 몇 블럭인지
        blocks = (x + 1) // (1 << (i + 1))
        # 블럭 개수 * 한 블럭 당 1의 개수
        cnt += blocks * (1 << i)
        
        # 블럭 처리 후 남은 수
        r = (x + 1) % (1 << (i + 1))
        
        # 남은 수가 반 블럭을 초과하면 1이 존재 
        # 예를들어 한 블럭이 8칸이면 반 블럭인 4칸을 초과해야 5번째 칸 부터 1이 있음
        # (ex. 0 0 0 0 1 1 1 1)
        if r > (1 << i):
            # 남은 수 - 반 블럭(2^i) 하면 1이 시작되는 수가 나오고 
            # 그 수부터 r까지의 모든 수는 i번째 자릿수가 항상 1임
            cnt += r - (1 << i)

    return cnt

result = count_ones_up_to(B) - count_ones_up_to(A - 1)
print(result)