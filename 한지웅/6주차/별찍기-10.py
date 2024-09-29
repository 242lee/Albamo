import math
from copy import deepcopy

# 틀렸는데요,, 왜 틀린지 몰라서 한번 같이 보면 좋을 것 같아요.

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
    scale = int(math.log(n,3))
    if scale == 1:
        print_matrix(s1)
        return
    if scale == 2:
        print_matrix(s2)
        return
    if scale == 3:
        print_matrix(s3)
        return
    if scale == 4:
        print_matrix(s4)
        return
    if scale == 5:
        print_matrix(s5)
        return
    if scale == 6:
        print_matrix(s6)
        return
    if scale == 7:
        print_matrix(s7)
        return
    if scale == 8:
        print_matrix(s8)
        return


s1 = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

s2 = make_default_matrix(s1, 3**2)
s2 = make_hole(s2, 3**2)

N = int(input())
scale = int(math.log(N,3))
if scale >= 3:
    s3 = make_default_matrix(s2, 3**3)
    s3 = make_hole(s3, 3**3)

if scale >= 4:
    s4 = make_default_matrix(s3, 3**4)
    s4 = make_hole(s4, 3**4)

if scale >= 5:
    s5 = make_default_matrix(s4, 3**5)
    s5 = make_hole(s5, 3**5)

if scale >= 6:
    s6 = make_default_matrix(s5, 3**6)
    s6 = make_hole(s6, 3**6)

if scale >= 7:
    s7 = make_default_matrix(s6, 3**7)
    s7 = make_hole(s7, 3**7)

if scale == 8:
    s8 = make_default_matrix(s7, 3**8)
    s8 = make_hole(s8, 3**8)

print_result(N)
