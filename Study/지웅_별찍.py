import math
from copy import deepcopy

# 틀렸는데요,, 왜 틀린지 몰라서 한번 같이 보면 좋을 것 같아요.

# 호진 >> 절대 log를 신용하지마!
# 해설: 243 입력하면 81의 결과가 나옴 -> 뭐가 문제일까 보니 
#       일관성을 깰만한 요소가 딱 >= 나 == 비교에 log가 쓰이는 걸 발견
#       0.0000....001 의 차이로 같아야할 수가 같지않아질 수 있음!
#       경계값에서 조건이 나뉘는 경우 log같은 소수가 반환되는 건 쓰지 않는 게 좋다~

def make_default_matrix(matrix, n):
    memory = []
    for j in matrix:
        new_j = []
        for cnt in range(3):
            for _ in range(len(j)):
                new_j.append(j[_])
        memory.append(new_j)

    ans = deepcopy(memory)
    for cnt in range(1,3):
        for i in memory:
            block = deepcopy(i)
            ans.append(block)
    return ans

def make_hole(matrix, n):
    ans = deepcopy(matrix)
    for i in range(int(n/3), int(2*n / 3)):
        for j in range(int(n/3), int(2*n / 3)):
            ans[i][j] = ' '
    return ans

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end='')
        print('')

def print_result(n):
    # scale = int(math.log(n,3))
    if N == 3**1:
        print_matrix(s1)
        return
    if N == 3**2:
        print_matrix(s2)
        return
    if N == 3**3:
        print_matrix(s3)
        return
    if N == 3**4:
        print_matrix(s4)
        return
    if N == 3**5:
        print_matrix(s5)
        return
    if N == 3**6:
        print_matrix(s6)
        return
    if N == 3**7:
        print_matrix(s7)
        return
    if N == 3**8:
        print_matrix(s8)
        return


s1 = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

s2 = make_default_matrix(s1, 3**2)
s2 = make_hole(s2, 3**2)

N = int(input())
# scale = int(math.log(N,3))
if N >= 3**3:
    s3 = make_default_matrix(s2, 3**3)
    s3 = make_hole(s3, 3**3)

if N >= 3**4:
    s4 = make_default_matrix(s3, 3**4)
    s4 = make_hole(s4, 3**4)

if N >= 3**5:
    s5 = make_default_matrix(s4, 3**5)
    s5 = make_hole(s5, 3**5)

if N >= 3**6:
    s6 = make_default_matrix(s5, 3**6)
    s6 = make_hole(s6, 3**6)

if N >= 3**7:
    s7 = make_default_matrix(s6, 3**7)
    s7 = make_hole(s7, 3**7)

if N == 3**8:
    s8 = make_default_matrix(s7, 3**8)
    s8 = make_hole(s8, 3**8)

print_result(N)
