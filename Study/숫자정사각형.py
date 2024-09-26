N, M = map(int,input().split())
# 정사각형을 찾아야 한다 and 가장 짧은 변 그 이상의 정사각형은 존재할 수 없다.
mx_size = min(N,M)
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input())))

# 아래에 존재하는 loop 이후, result값의 변화가 없다면 1을 도출해야함.
result = 1


# 값 4개를 받고, 이 4가지 값이 동일한지 판단하는 함수
def value_check(a,b,c,d):
    if a == b == c == d:
        return True
    return False

# size를 입력받으면, 해당 size가 문제의 조건을 만족하는지 판단하는 함수
def check_function(size):
    for i in range(N-size+1):
        for j in range(M-size+1):
            left_top = (i,j)
            right_top = (i, j+size-1)
            left_bottom = (i+size-1, j)
            right_bottom = (i+size-1, j+size-1)
            check_result = value_check(matrix[left_top[0]][left_top[1]], matrix[left_bottom[0]][left_bottom[1]], matrix[right_top[0]][right_top[1]], matrix[right_bottom[0]][right_bottom[1]])
            if check_result == True:
                return True
    return False

# size를 가능한 최대 사이즈까지 늘려가며 확인하는 반복과정
for rec_size in range(2, mx_size + 1):
    after_check = check_function(rec_size)
    if after_check == True:
        result = rec_size

print(result ** 2)
